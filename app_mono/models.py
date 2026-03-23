from django.db import models


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    aktywna = models.BooleanField(default=True)

    class Meta:
        ordering = ['nazwa']
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):
    kategoria = models.ForeignKey(
        Kategoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produkty'
    )
    nazwa = models.CharField(max_length=200)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dostepny = models.BooleanField(default=True)
    data_dodania = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_dodania']
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return self.nazwa


class Zamowienie(models.Model):
    class Status(models.TextChoices):
        NOWE = 'nowe', 'Nowe'
        W_REALIZACJI = 'w_realizacji', 'W realizacji'
        ZREALIZOWANE = 'zrealizowane', 'Zrealizowane'
        ANULOWANE = 'anulowane', 'Anulowane'

    klient_imie = models.CharField(max_length=100)
    klient_email = models.EmailField()
    data_zamowienia = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOWE
    )
    uwagi = models.TextField(blank=True)
    suma = models.DecimalField(max_digits=10, decimal_places=2)
    produkty = models.ManyToManyField(Produkt, related_name='zamowienia')

    class Meta:
        ordering = ['-data_zamowienia']
        verbose_name = 'Zamówienie'
        verbose_name_plural = 'Zamówienia'

    def __str__(self):
        return f'Zamówienie #{self.pk} – {self.klient_imie}'
