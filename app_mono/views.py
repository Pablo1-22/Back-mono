from django.shortcuts import render, get_object_or_404

from .models import Kategoria, Produkt, Zamowienie


def produkt_list(request):
    produkty = Produkt.objects.all()
    return render(
        request,
        'app_mono/produkt/list.html',
        {'produkty': produkty}
    )


def kategoria_list(request):
    kategorie = Kategoria.objects.all()
    return render(
        request,
        'app_mono/kategoria/list.html',
        {'kategorie': kategorie}
    )


def kategoria_detail(request, pk):
    kategoria = get_object_or_404(Kategoria, pk=pk)
    produkty = kategoria.produkty.all()
    return render(
        request,
        'app_mono/kategoria/detail.html',
        {'kategoria': kategoria, 'produkty': produkty}
    )


def zamowienie_list(request):
    zamowienia = Zamowienie.objects.all()
    return render(
        request,
        'app_mono/zamowienie/list.html',
        {'zamowienia': zamowienia}
    )
