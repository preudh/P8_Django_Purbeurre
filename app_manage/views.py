from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from app_data_off.models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


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
    if request.GET:
        user = request.user
        query = request.GET.get('q')
        food = Product.objects.filter(name__icontains=query)[:1]
        foo = get_object_or_404(Product)
        substitute_list = []
        if foo.nutrition_grade == 'a':
            substitute_list = Product.objects.filter(Q(name__icontains=query) & Q
            (category_tags2__icontains=foo.category) & Q
                                                     (nutri_score__lte=foo.nutrition_grade))

        if foo.nutrition_grade == 'b':
            substitute_list = Product.objects.filter(Q(name__icontains=query) & Q
            (category_tags2__icontains=foo.category) & Q
                                                     (nutri_score__lte=foo.nutrition_grade))

        if foo.nutrition_grade == 'c':
            substitute_list = Product.objects.filter(Q(name__icontains=query) & Q
            (category_tags2__icontains=foo.category) & Q
                                                     (nutri_score__lt=foo.nutrition_grade))
        if foo.nutrition_grade == 'd':
            substitute_list = Product.objects.filter(Q(name__icontains=query) & Q
            (category_tags2__icontains=foo.category) & Q
                                                     (nutri_score__lt=foo.nutrition_grade))
        if foo.nutrition_grade == 'e':
            substitute_list = Product.objects.filter(Q(name__icontains=query) & Q
            (category_tags2__icontains=foo.category) & Q
                                                     (nutri_score__lt=foo.nutrition_grade))
        if len(substitute_list) == 0:
            try:
                substitute_list = Product.objects.filter(Q(category_tags2__icontains=foo.category) & Q
                (nutri_score__lt=foo.nutrition_grade))
            except:
                pass
        substitute_list = substitute_list.order_by('nutrition_grade')
        substitute_list = substitute_list.exclude(name=foo.name)
        favori = Product.objects.filter(Q(backup__user_id=user.id))

        # paginator settings
        page = request.GET.get('page')
        paginator = Paginator(substitute_list, 6)
        try:
            substitute = paginator.page(page)
        except PageNotAnInteger:
            substitute = paginator.page(1)
        except EmptyPage:
            substitute = paginator.page(paginator.num_pages)
        context = {
            'favori': favori,
            'foods': Product,
            'substitute': substitute,
            'paginate': True,
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'index.html')


def details(request, food_id):
    form = SearchForm(request.POST)
    food = get_object_or_404(Product, id=food_id)
    context = {
        'Product': food,
        'form': form
    }
    return render(request, 'details.html', context)
