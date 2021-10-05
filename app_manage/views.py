from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# instead of the model’s DoesNotExist exception.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q  # Complex queries with Q objects
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.contrib import messages
# personal import
from app_data_off.models import Product, Category


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
        if search in ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner']:
            fk_category=Category.objects.get(name=search)
            product=Product.objects.filter(category_id=fk_category.pk)
            p1 = Product.objects.filter(category_id=fk_category.pk).first()
            return render(request, 'search.html', context={"product": product, "p1": p1})

        product=Product.objects.filter(name__icontains=search)
        p1=Product.objects.filter(name=search).first()
        return render(request, 'search.html', context={"product": product, "p1": p1})

#
# def save_substitut(request):
#     """ Route to get save product Ajax script. Return confirmation or error message. """
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
