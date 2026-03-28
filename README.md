# Kup mnie – sklep internetowy (monolit)

Prosta aplikacja sklepu internetowego zbudowana w Django. Umożliwia przeglądanie produktów, kategorii oraz zamówień. Projekt realizowany w ramach przedmiotu Programowanie Back-end.

## Funkcjonalności

- Lista produktów z ceną, opisem i statusem dostępności
- Kategorie produktów z możliwością filtrowania
- Lista zamówień
- Panel administracyjny Django

## Wymagania

- Python 3.10+
- pip

## Uruchomienie

1. **Aktywuj wirtualne środowisko:**
   ```bash
   venv/Scripts/activate
   ```

2. **Zainstaluj zależności:**
   ```bash
   cd Back_mono
   pip install -r requirements.txt
   ```

3. **Wykonaj migracje bazy danych:**
   ```bash
   python manage.py migrate
   ```

4. **Uruchom serwer deweloperski:**
   ```bash
   python manage.py runserver
   ```

5. **Otwórz w przeglądarce:**
   - Aplikacja: http://127.0.0.1:8000/app_mono/
   - Panel admina: http://127.0.0.1:8000/admin/

## Technologie

- Python 3
- Django 6.0
- SQLite
- HTML/CSS (własny motyw ciemny)
