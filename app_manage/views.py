from django.shortcuts import render, get_object_or_404, redirect  # Calls get() on a given model manager, but it raises Http404
# instead of the model’s DoesNotExist exception.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q  # Complex queries with Q objects
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from django.contrib import messages
# personal import
from app_data_off.models import Product, Category
from app_manage.models import Cart, Order
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


def search_substitut(name):
    Category.objects.filter (name_contains = )







# @login_required
def add_to_substitute(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity is updated")
            return redirect("home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item is addedd to your cart")
            return redirect("home")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item is added to your cart")
        return redirect("home")


class Substitute(ListView):
    model = Product
    template_name = 'substitute.html'


class Detail(DetailView):
    model = Product
    template_name = 'details.html'


# @login_required
# def add_to_favorite(request, pk):
#     pass
