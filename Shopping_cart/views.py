from django.shortcuts import render, redirect
from .car import Car
from store.models import productModel

# Create your views here.

def addProduct(request, product_id):
    car = Car(request)
    varProduct= productModel.objects.get(id= product_id)
    car.addProduct(product=varProduct)
    return redirect("myCar")


def deleteProduct(request, product_id):
    car = Car(request)
    varProduct=productModel.objects.get(id= product_id)
    car.delete(product=varProduct)
    return redirect("myCar")

def restProduct(request, product_id):
    car = Car(request)
    varProduct=productModel.objects.get(id= product_id)
    car.restProduct(product=varProduct)
    return redirect("myCar")

def cleanCar(request):
    car = Car(request)
    car.cleanCar()
    return car
