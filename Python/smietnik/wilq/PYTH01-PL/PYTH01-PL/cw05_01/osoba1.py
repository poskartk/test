import datetime


class Osoba:
    """
    Klasa reprezentuje osoby.

    Wszystkie atrybuty są publiczne.
    Brak kontroli danych może doprowadzić do niespójności danych.
    """
    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec  # wartość logiczna: True - mężczyzna, False - kobieta
        self.rok_urodzenia = rok_urodzenia

    # Metoda zwraca informację o płci: M - mężczyzna, K - kobieta
    def jaka_plec(self):
        return "M" if self.plec else "K"

    def jaki_rok_urodzenia(self):
        return self.rok_urodzenia

    # Metoda wylicza aktualny wiek
    def ile_lat(self):
        return datetime.date.today().year - self.rok_urodzenia

    # Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
    def __str__(self):
        return f'{self.imie} {self.nazwisko}, płeć: {self.jaka_plec()}, wiek: {self.ile_lat()} lat'


# utworzenie osoby
jk = Osoba('Jan', 'Kowalski', True, 1990)
# sprawdzenie wartości atrybutów obiektu osoby
print('IMIĘ:', jk.imie)
print('NAZWISKO:', jk.nazwisko)
print('KOMPLETNY OPIS:', jk, end='\n\n')

# utworzenie osoby
an = Osoba('Anna', 'Nowak', False, 2001)
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)

# korekta roku urodzenia o 1 (odmłodzenie o 1 rok)
an.rok_urodzenia += 1
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)

# zmiana roku urodzenia na podaną wartość
an.rok_urodzenia = 2025
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)
