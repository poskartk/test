import datetime


class Osoba:
    """
    Klasa reprezentuje osoby.

    W klasie zdefiniowano właściwości.
    """
    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        self.__ustaw_imie(imie)
        self.__ustaw_nazwisko(nazwisko)
        self.__ustaw_plec(plec)
        self.__ustaw_rok_urodzenia(rok_urodzenia)

    # -------------------------------------------------------
    # Metody dostępowe do odczytu atrybutów - gettery
    # -------------------------------------------------------
    def __jakie_imie(self):
        return self.__imie

    def __jakie_nazwisko(self):
        return self.__nazwisko

    # Metoda zwraca informację o płci: M - mężczyzna, K - kobieta
    def __jaka_plec(self):
        return "M" if self.__plec else "K"

    def __jaki_rok_urodzenia(self):
        return self.__rok_urodzenia

    # -------------------------------------------------------
    # metody dostępowe do ustawiania atrybutów - settery
    # -------------------------------------------------------

    # metoda dodatkowo sprawdza, czy podane imię nie jest puste
    def __ustaw_imie(self, imie):
        if imie:
            self.__imie = imie
        else:
            print('....... Zmiana imienia odrzucona (imię nie może być puste)')

    # metoda dodatkowo sprawdza, czy podane nazwisko nie jest puste
    def __ustaw_nazwisko(self, nazwisko):
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            print('....... Zmiana nazwiska odrzucona (nazwisko nie może być puste)')

    def __ustaw_plec(self, plec):
        self.__plec = plec

    # metoda dodatkowo sprawdza, czy podany rok urodzenia już nadszedł
    def __ustaw_rok_urodzenia(self, rok_urodzenia):
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            print('....... Zmiana roku urodzenia odrzucona (rok jeszcze nie nadszedł)')


    imie = property(__jakie_imie, __ustaw_imie)
    nazwisko = property(__jakie_nazwisko, __ustaw_nazwisko)
    plec = property(__jaka_plec, __ustaw_plec)
    rok_urodzenia = property(__jaki_rok_urodzenia, __ustaw_rok_urodzenia)

    # Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
    def __str__(self):
        return f'{self.__imie} {self.__nazwisko}, płeć: {self.__plec}, wiek: {self.ile_lat()} lat'

    def ile_lat(self):
        return datetime.date.today().year - self.rok_urodzenia


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
