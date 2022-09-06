from django.shortcuts import render
from store.models import productCategory, productModel


# Create your views here.

def store(request):
    varStore = productModel.objects.all()
    return render(request, 'Store/store.html', {'varStore': varStore})

def shopping(request):
    return render(request, 'Store/car/shopping_cart.html')