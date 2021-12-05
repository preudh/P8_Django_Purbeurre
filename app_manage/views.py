from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# personal import
from app_data_off.models import Product, Category, UserProduct
from app_data_off.management.commands.constante import list_categories


# Create your views here.

def base(request):
    return render(request, '../templates/base.html')


def termes(request):
    return render(request, 'termes.html')


def index(request):
    form=SearchForm(request.POST)
    context={
        'form': form
    }
    return render(request, 'index.html', context)


def search(request):
    # if this is a POST request we need to process the form data

    if request.method == "POST":
        search=request.POST.get('search')
        if search in list_categories:

            # gets the category in the database which name equals to search and result is
            # assigned to the fk_category variable
            fk_category=Category.objects.get(name=search)

            # get the first product of the category above
            p1=Product.objects.filter(category_id=fk_category.id).first()

            # get all products ordered by nutriscore of the category
            # type Queryset and then SQL generated when affected to variable
            # products=Product.objects.filter(category_id=fk_category.id).order_by('nutrition_grade')
            products=fk_category.product_set.all().order_by("nutrition_grade")

            # Paginator class to split the results of products variable into pages and each page has only 6 products
            paginator=Paginator(products, 6)  # products = cache = None!

            # request.GET contains GET variables and appear in the address bar,e.g http://127.0.0.1:8000/?page=2
            # The .get() is a python method used to return the value of items with a specific key from
            # a dictionary. If nothing is found None is returned.
            # if the url of the GET request has 'page' parameter, get it. If it does not, return 1 by default.
            # so get the value of a GET variable that has a name of 'page' and then assign that to page_number variable
            page_number=request.GET.get('page', 1)  # ok
            try:
                # returns a Page object and If the page isn’t a number, it returns the first page.
                page_obj=paginator.page(page_number)  # ok
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                page_obj=paginator.page(1)
            except EmptyPage:
                # If page is out of range
                # Delivery last page of results
                page_obj=paginator.page(paginator.num_pages)

        else:
            # products=Product.objects.filter(name__icontains=search).order_by('nutrition_grade')
            products=Product.objects.filter(name__icontains=search).order_by('nutrition_grade')
            p1=Product.objects.filter(name__icontains=search).first()

            paginator=Paginator(products, 6)
            page_number=request.GET.get('page', 1)
            try:
                page_obj=paginator.page(page_number)
            except PageNotAnInteger:
                page_obj=paginator.page(1)
            except EmptyPage:
                page_obj=paginator.page(paginator.num_pages)

        context={
            'products': page_obj,
            'p': p1,
            # 'paginate': True,
            'list_categories': list_categories,
        }
        return render(request, 'search.html', context)


def detail(request, product_id):
    form=SearchForm(request.POST)
    p=get_object_or_404(Product, id=product_id)
    context={
        'p': p,
        'form': form
    }
    return render(request, 'detail.html', context)


@login_required(login_url='/login/')
# @login_required()
def save(request, product_id):
    """ . """
    if request.method == 'POST':
        user_id=request.user.id
        user_product=UserProduct.objects.filter(product_id=product_id, user_id=user_id)
        if not user_product.exists():
            UserProduct.objects.create(product_id=product_id, user_id=user_id)
        else:
            return redirect("index")
    # By default, redirect () returns a temporary redirect. All of the above forms accept a permanent parameter which,
    # if set to True, produces a permanent redirect:
    return redirect('/index', permanent=True)


@login_required(login_url='/login/')
# @login_required()
def favorite(request):
    user_id=request.user.id
    fav_products=UserProduct.objects.filter(user_id=user_id)
    # page=request.GET.get('page', 1)
    if fav_products.exists():
        products=[]
        for fav_product in fav_products:
            product=Product.objects.get(id=fav_product.product_id)
            if product not in products:
                products.append(product)
    else:
        return redirect('/index', permanent=True)

    # paginator=Paginator(products, 10)
    # try:
    #     products=paginator.page(page)
    # except PageNotAnInteger:
    #     products=paginator.page(1)
    # except EmptyPage:
    #     products=paginator.page(paginator.num_pages)
    context={
        'favori': products,
        # 'paginate': True,
        # 'favoris': favoris
    }
    return render(request, 'favorite.html', context)


@login_required(login_url='/login/')
def remove_favorite(request, pk):
    user_id=request.user.id
    fav_products=UserProduct.objects.filter(user_id=user_id)

    if fav_products.exists():
        remove_fav=fav_products.get(product_id=pk)
        remove_fav.delete()
        return redirect('/favorite')
    else:
        return redirect('/index', permanent=True)
