from django.urls import path

from . import views

app_name = 'app_mono'

urlpatterns = [
    path('', views.produkt_list, name='produkt_list'),
    path('kategorie/', views.kategoria_list, name='kategoria_list'),
    path('zamowienia/', views.zamowienie_list, name='zamowienie_list'),
]
