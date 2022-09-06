from django.urls import path
from finalProject.settings import MEDIA_ROOT, MEDIA_URL
from finalProjectApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name='Home'),

]

urlpatterns+=static(MEDIA_URL, document_root=MEDIA_ROOT)
