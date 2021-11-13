from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.contrib import messages
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


# def load_categories(request):
#     return render(request, 'search.html', {'list_categories': list_categories})


def search(request):
    # if this is a POST request we need to process the form data

    if request.method == "POST":
        search=request.POST.get('search')
        if search in list_categories:
            fk_category=Category.objects.get(name=search)
            p1=Product.objects.filter(category_id=fk_category.pk).first()

            products=Product.objects.filter(category_id=fk_category.pk).order_by('nutrition_grade')
            # paginator settings - pagination with only 6 products by page
            paginator=Paginator(products, 6)
            page_number=request.GET.get('page')
            try:
                page_obj=paginator.page(page_number)
            except PageNotAnInteger:
                page_obj=paginator.page(1)
            except EmptyPage:
                page_obj=paginator.page(paginator.num_pages)
            context={
                'products': page_obj,
                'p': p1,
                'list_categories': list_categories,
                'paginate': True,
            }
            return render(request, 'search.html', context)

        products=Product.objects.filter(name__icontains=search).order_by('nutrition_grade')
        p1=Product.objects.filter(name__icontains=search).first()

        # paginator settings - pagination with only 6 products by page
        paginator=Paginator(products, 6)
        page_number=request.GET.get('page')
        try:
            page_obj=paginator.page(page_number)
        except PageNotAnInteger:
            page_obj=paginator.page(1)
        except EmptyPage:
            page_obj=paginator.page(paginator.num_pages)
        context={
            'products': page_obj,
            'p': p1,
            'paginate': True,
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

    if fav_products.exists():
        products=[]
        for fav_product in fav_products:
            product=Product.objects.get(id=fav_product.product_id)
            if product not in products:
                products.append(product)

    else:
        return redirect('/index', permanent=True)

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
        messages.warning(request, "Cet aliment est retiré de vos substituts")
        return redirect('/favorite')
    else:
        return redirect('/index', permanent=True)
