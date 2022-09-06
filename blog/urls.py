from django.urls import path
from blog import views

urlpatterns = [
    path('', views.Blog, name='Blog'),
    path('category/<categories_id>/', views.category, name='Category'),
]