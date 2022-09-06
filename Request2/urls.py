from django.urls import path
from Request2 import views


urlpatterns = [
    path('', views.processRequest, name="productRequest"),
]