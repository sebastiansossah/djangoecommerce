from django.urls import path
from Shopping_cart import views

app_name="car"

urlpatterns = [
    path('add/<int:product_id>/', views.addProduct, name="add"),
    path('delete/<int:product_id>/', views.deleteProduct, name="delete"),
    path('restProduct/<int:product_id>/', views.restProduct, name="rest"),
    path('clean/<int:product_id>/', views.cleanCar, name="clean"),
]