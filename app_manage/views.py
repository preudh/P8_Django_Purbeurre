from django.shortcuts import render
from .forms import SearchForm


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
