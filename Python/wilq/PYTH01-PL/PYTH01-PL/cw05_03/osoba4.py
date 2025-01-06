import datetime


class Osoba:
    """
    Klasa reprezentuje osoby.

    W klasie zdefiniowano właściwości.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__plec = plec
        self.__rok_urodzenia = rok_urodzenia

    # -------------------------------------------------------
    # Metody dostępowe do odczytu atrybutów - gettery
    # -------------------------------------------------------
    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    # Metoda zwraca informację o płci: M - mężczyzna, K - kobieta
    @property
    def plec(self):
        return "M" if self.__plec else "K"

    @property
    def rok_urodzenia(self):
        return self.__rok_urodzenia

    # -------------------------------------------------------
    # metody dostępowe do ustawiania atrybutów - settery
    # -------------------------------------------------------

    # metoda dodatkowo sprawdza czy podane imię nie jest puste
    @imie.setter
    def imie(self, imie):
        if imie:
            self.__imie = imie
        else:
            print('....... Zmiana imienia odrzucona (imię nie może być puste)')

    # metoda dodatkowo sprawdza czy podane nazwisko nie jest puste
    @nazwisko.setter
    def nazwisko(self, nazwisko):
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            print('....... Zmiana nazwiska odrzucona (nazwisko nie może być puste)')

    @plec.setter
    def plec(self, plec):
        self.__plec = plec

    # metoda dodatkowo sprawdza czy podany rok urodzenia już nadszedł
    @rok_urodzenia.setter
    def rok_urodzenia(self, rok_urodzenia):
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            print('....... Zmiana roku urodzenia odrzucona (rok jeszcze nie nadszedł)')

    # Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
    def __str__(self):
        return f'{self.imie} {self.nazwisko}, płeć: {self.plec}, wiek: {self.ile_lat()} lat'

    def ile_lat(self):
        return datetime.date.today().year - self.__rok_urodzenia


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

# zmiana roku urodzenia o 1 (odmłodzenie)
an.rok_urodzenia += 1
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)

# korekta roku urodzenia o 1 (odmłodzenie o 1 rok)
an.rok_urodzenia = 2025
# sprawdzenie wartości atrybutów obiektu osoby
print('KOMPLETNY OPIS:', an)
