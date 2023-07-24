from django.urls import path
from app.views import index, get_xamshira, get_doktor, get_xona, get_klient

urlpatterns = [
    path('', index, name='home'),
    path('get_doktor/', get_doktor, name='get_doktor'),
    path('get_xona/', get_xona, name='get_xona'),
    path('get_klient/', get_klient, name='get_klient'),
    path('get_klient/<int:pk>/', get_klient, name='get_klient'),
    path('get_xamshira/', get_xamshira, name='get_xamshira'),
]
