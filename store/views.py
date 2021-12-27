from django.shortcuts import render
from store.models import Product

# Create your views here.


def index(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'store/product_list.html', context)


def show(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'store/product.html', context)
