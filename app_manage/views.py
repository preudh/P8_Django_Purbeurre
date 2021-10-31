from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from app_users.views import login_request
# instead of the model’s DoesNotExist exception.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q  # Complex queries with Q objects
from .forms import SearchForm
from django.contrib import messages
# personal import
from app_data_off.models import Product, Category, UserProduct


# Create your views here.

def base(request):
    return render(request, '../templates/base.html')


def termes(request):
    return render(request, 'termes.html')


def index(request):
    form = SearchForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def search(request):
    # if this is a POST request we need to process the form data

    if request.method == "POST":
        search = request.POST.get('search')
        if search in ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner']:
            fk_category = Category.objects.get(name=search)
            product = Product.objects.filter(category_id=fk_category.pk)
            # print(product)
            p1 = Product.objects.filter(category_id=fk_category.pk).first()
            return render(request, 'search.html', context={"product": product, "p1": p1})

        product = Product.objects.filter(name__icontains=search)
        p1 = Product.objects.filter(name=search).first()
        return render(request, 'search.html', context={"product": product, "p1": p1})


def detail(request, product_id):
    form = SearchForm(request.POST)
    p = get_object_or_404(Product, id=product_id)
    context = {
        'p': p,
        'form': form
    }
    return render(request, 'detail.html', context)


@login_required(login_url='/login/')
# @login_required()
def save(request, product_id, ):
    """ . """
    if request.method == 'POST':
        user_id = request.user.id
        user_product = UserProduct.objects.filter(product_id=product_id, user_id=user_id)
        if not user_product.exists():
            UserProduct.objects.create(product_id=product_id, user_id=user_id)
        else:
            return redirect("search")
    return redirect('/index', permanent=True)


@login_required(login_url='/login/')
# @login_required()
def favorite(request):
    user_id = request.user.id
    fav_products = UserProduct.objects.filter(user_id=user_id)

    if fav_products.exists():
        products = []
        for fav_product in fav_products:
            product = Product.objects.get(id=fav_product.product_id)
            if product not in products:
                products.append(product)

    else:
        return redirect('/index', permanent=True)

    context = {
        'favori': products,
        # 'paginate': True,
        # 'favoris': favoris
    }
    return render(request, 'favorite.html', context)


@login_required(login_url='/login/')
def remove_favorite(request, pk):
    user_id = request.user.id
    fav_products = UserProduct.objects.filter(user_id=user_id)

    if fav_products.exists():
        # remove_fav = fav_products.get(id=fav_products.pk)
        remove_fav = fav_products.get(product_id=pk)
        remove_fav.delete()
        messages.warning(request, "Cet aliment est retiré de vos substituts")
        return redirect('/favorite')
    else:
        return redirect('/index', permanent=True)



# def search(request):  # essai 2 dont work
#     # if this is a POST request we need to process the form data
#
#     if request.method == "POST":
#         search=request.POST.get('search')
#         if search in ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner']:
#             fk_category=Category.objects.get(name=search)
#             list_product=[]
#             product=Product.objects.filter(category_id=fk_category.pk)
#             p1=Product.objects.filter(category_id=fk_category.pk).first()
#             for entry in product:
#                 list_product.append(entry)
#                 return render(request, 'search.html', context={"p": entry, "p1": p1})
#
#         list_product=[]
#         product=Product.objects.filter(name__icontains=search)
#         for entry in product:
#             list_product.append(entry)
#             return render(request, 'search.html', context={"p": entry, "p1": p1})


# def search(request):
# #     # if this is a POST request we need to process the form data
# #
#     if request.method == "POST":
#         search=request.POST.get('search')
#         if search in ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner']:
#             fk_category=Category.objects.get(name=search)
#             list_product=[]
#             product=Product.objects.filter(category_id=fk_category.pk).order_by('id')
#             paginator=Paginator(list_product, 6)  # new Show 6 products per page.
#             page_number=request.GET.get('page')  # new
#             page_obj=paginator.get_page(page_number)  # new
#             list_product=[entry for entry in product]
#             # for entry in product:
#             #     list_product.append(entry)
#             print(product)  # new + order by id
#             print(list_product)
#             print(type(list_product)) # liste d'instance de class!
#             p1 = Product.objects.filter(category_id=fk_category.pk).first()
#             # paginator=Paginator(list_product, 6)  # new Show 6 products per page.
#             # page_number=request.GET.get('page')  # new
#             # page_obj=paginator.get_page(page_number)  # new
#             return render(request, 'search.html', context={"product": list_product, "p1": p1, 'page_obj': page_obj}) # new
#
#         product=Product.objects.filter(name__icontains=search).order_by('id')  # new + order by id
#         paginator=Paginator(product, 6)  # new Show 6 products per page.
#         page_number=request.GET.get('page')  # new
#         page_obj=paginator.get_page(page_number)  # new
#         p1=Product.objects.filter(name=search).first()
#         # paginator=Paginator(product, 6)  # new Show 6 products per page.
#         # page_number=request.GET.get('page')  # new
#         # page_obj=paginator.get_page(page_number)  # new
#         return render(request, 'search.html', context={"product": product, "p1": p1, 'page_obj': page_obj})  # new


# #
# def save(request):
#     """ save product. Return confirmation or error message. """
#
#     response_data = {}
#
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         product_id = request.POST.get('product_id')
#
#         fav_product_for_current_user = FavouriteProduct.objects.filter(product_id=product_id, user_id=user_id)
#         if not fav_product_for_current_user.exists():
#             FavouriteProduct.objects.create(product_id=product_id, user_id=user_id)
#             response_data['success_message'] = 'Produit sauvegardé'
#         else:
#             response_data['error_message'] = 'Produit déjà sauvegardé'
#
#     else:
#         response_data['error_message'] = 'Impossible de sauvegarder le produit'
#
#     return HttpResponse(
#         json.dumps(response_data),
#         content_type='application/json',
#     )
