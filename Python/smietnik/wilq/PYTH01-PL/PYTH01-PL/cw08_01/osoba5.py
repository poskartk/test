import datetime


class Osoba:
    """
    Klasa definiuje osobę.

    W klasie zdefiniowano właściwości.
    """

    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.rok_urodzenia = rok_urodzenia

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
            raise ValueError('Imię nie może być puste')

    # metoda dodatkowo sprawdza, czy podane nazwisko nie jest puste
    def __ustaw_nazwisko(self, nazwisko):
        if nazwisko:
            self.__nazwisko = nazwisko
        else:
            raise ValueError('Nazwisko nie może być puste')

    def __ustaw_plec(self, plec):
        if isinstance(plec, bool):
            self.__plec = plec
        else:
            raise TypeError('Płeć musi byc wartością logiczną')

    # metoda dodatkowo sprawdza, czy podany rok urodzenia już nadszedł
    def __ustaw_rok_urodzenia(self, rok_urodzenia):
        if rok_urodzenia < datetime.date.today().year:
            self.__rok_urodzenia = rok_urodzenia
        else:
            raise ValueError('Rok urodzenia jeszcze nie nadszedł')

    imie = property(__jakie_imie, __ustaw_imie)
    nazwisko = property(__jakie_nazwisko, __ustaw_nazwisko)
    plec = property(__jaka_plec, __ustaw_plec)
    rok_urodzenia = property(__jaki_rok_urodzenia, __ustaw_rok_urodzenia)

    # Metoda konwersji obiektu osoby na postać tekstową (zwraca pełny opis obiektu)
    def __str__(self):
        return f'{self.__imie} {self.__nazwisko}, płeć: {self.__plec}, wiek: {self.ile_lat()} lat'

    def ile_lat(self):
        return datetime.date.today().year - self.__rok_urodzenia


# Funkcja pomocnicza
# Próbuje utworzyć osobę i informuje o powodzeniu lub o problemach
def utworz_osobe(imie, nazwisko, plec, rok_urodzenia):
    try:
        osoba = Osoba(imie, nazwisko, plec, rok_urodzenia)
    except ValueError as e:
        print('WYJĄTEK:', e)
    except TypeError:
        print('WYJĄTEK: Błędny typ danych')
    else:
        print('OK:     ', osoba)


# Test
utworz_osobe('Jan', 'Kowalski', True, 1990)  # poprawne utworzenie osoby
utworz_osobe(None, 'Kowalski', True, 1990)  # błędne utworzenie osoby — brak imienia
utworz_osobe('Jan', '', True, 1990)  # błędne utworzenie osoby — brak nazwiska
utworz_osobe('Jan', 'Kowalski', 1, 1990)  # błędna wartość płci
utworz_osobe('Jan', 'Kowalski', True, 2025)  # błędna wartość roku urodzenia
utworz_osobe('Jan', 'Kowalski', True, '1990')  # błędna typ roku urodzenia
