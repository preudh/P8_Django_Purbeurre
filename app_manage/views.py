from django.shortcuts import render, get_object_or_404, redirect  # Calls get() on a given model manager, but it raises Http404
# instead of the model’s DoesNotExist exception.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q  # Complex queries with Q objects
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.contrib import messages
# personal import
from app_data_off.models import Product, Category
from app_manage.models import Substitut, SaveSubstitut
from django.views.generic import ListView, DetailView


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


def search_substitut(search):

    if search in ['Viandes', 'Poissons', 'Epicerie', 'Chocolats', 'Pates-a-tartiner']:
        fk_category = Category.objects.filter(name=search)
        return Product.objects.filter(category=fk_category)

    return Product.objects.filter(name=search)


def save_substitut(request):
    """ Route to get save product Ajax script. Return confirmation or error message. """

    response_data = {}

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        product_id = request.POST.get('product_id')

        fav_product_for_current_user = FavouriteProduct.objects.filter(product_id=product_id, user_id=user_id)
        if not fav_product_for_current_user.exists():
            FavouriteProduct.objects.create(product_id=product_id, user_id=user_id)
            response_data['success_message'] = 'Produit sauvegardé'
        else:
            response_data['error_message'] = 'Produit déjà sauvegardé'

    else:
        response_data['error_message'] = 'Impossible de sauvegarder le produit'

    return HttpResponse(
        json.dumps(response_data),
        content_type='application/json',
    )



#
#
#
#
#
#
# class Substitute(ListView):
#     model = Product
#     template_name = 'substitute.html'
#
#
# class Detail(DetailView):
#     model = Product
#     template_name = 'details.html'
#
#
# # @login_required
# # def add_to_favorite(request, pk):
# #     pass
