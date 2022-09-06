from django.urls import path
from authentication.views import Vregister, closeSession, theLoger

urlpatterns = [
    path('', Vregister.as_view() , name='authentication'),
    path('closeSession', closeSession , name='logout'),
    path('login', theLoger , name='login'),
]