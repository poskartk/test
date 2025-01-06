import datetime


class Osoba:
    """
    Klasa reprezentuje osoby.

    Klasa jest shermetyzowana - kłopotliwa aktualizacja danych.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        self.ustaw_imie(imie)
        self.ustaw_nazwisko(nazwisko)
        self.ustaw_plec(plec)
        self.ustaw_rok_urodzenia(rok_urodzenia)

    # -------------------------------------------------------
    # Metody dostępowe do odczytu atrybutów - gettery
    # -------------------------------------------------------
    def jakie_imie(self):
        return self.__imie

    def jakie_nazwisko(self):
        return self.__nazwisko

    # Metoda zwraca informację o płci: M - mężczyzna, K - kobieta
    def jaka_plec(self):
        return "M" if self.__plec else "K"

    def jaki_rok_urodzenia(self):
        return self.__rok_urodzenia

    # -------------------------------------------------------
    # metody dostępowe do ustawiania atrybutów - settery
    # -------------------------------------------------------

    # metoda dodatkowo sprawdza, czy podane imię nie jest puste
    def ustaw_imie(self, imie):
        if imie:
            self.__imie = imie
        else:
            print('....... Zmiana imienia odrzucona (imię nie może być puste)')

    # metoda dodatkowo sprawdza, czy podane nazwisko nie jest puste
    def ustaw_nazwisko(self, nazwisko):
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            print('....... Zmiana nazwiska odrzucona (nazwisko nie może być puste)')

    def ustaw_plec(self, plec):
        self.__plec = plec

    # metoda dodatkowo sprawdza, czy podany rok urodzenia już nadszedł
    def ustaw_rok_urodzenia(self, rok_urodzenia):
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            print('....... Zmiana roku urodzenia odrzucona (rok jeszcze nie nadszedł)')

    # Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
    def __str__(self):
        return f'{self.__imie} {self.__nazwisko}, płeć: {self.jaka_plec()}, wiek: {self.ile_lat()} lat'

    def ile_lat(self):
        return datetime.date.today().year - self.__rok_urodzenia


# utworzenie osoby
jk = Osoba('Jan', 'Kowalski', True, 1990)
# sprawdzenie wartości atrybutów obiektu osoby
print('IMIĘ:', jk.jakie_imie())
print('NAZWISKO:', jk.jakie_nazwisko())
print('KOMPLETNY OPIS:', jk, end='\n\n')

# utworzenie osoby
an = Osoba('Anna', 'Nowak', False, 2001)
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)

# korekta roku urodzenia o 1 (odmłodzenie o 1 rok)
an.ustaw_rok_urodzenia(an.jaki_rok_urodzenia() + 1)  # wygląda koszmarnie...
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)

# zmiana roku urodzenia na podaną wartość
an.ustaw_rok_urodzenia(2025)
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)
