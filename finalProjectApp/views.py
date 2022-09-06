from django.shortcuts import render

from Shopping_cart.car import Car


# Create your views here.


def Home(request):
    car= Car(request)
    print(car)
    return render(request, 'finalProjectApp/home.html')



