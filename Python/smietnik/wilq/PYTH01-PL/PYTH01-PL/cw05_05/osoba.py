class Osoba:
    """
    Klasa definiuje osobę.
    """
    def __init__(self, imie, nazwisko, plec, rok_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec  # wartość logiczna: True - mężczyzna, False - kobieta
        self.rok_urodzenia = rok_urodzenia

    def __lt__(self, other):
        return self.nazwisko < other.nazwisko if self.nazwisko != other.nazwisko else self.imie < other.imie

    def __gt__(self, other):
        return self.nazwisko > other.nazwisko if self.nazwisko != other.nazwisko else self.imie > other.imie

    def __eq__(self, other):
        return self.nazwisko == other.nazwisko and self.imie == other.imie

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'


def porownaj(osoba1, osoba2):
    if osoba1 < osoba2:
        print(f'{osoba1} <  {osoba2}')
    elif osoba1 == osoba2:
        print(f'{osoba1} == {osoba2}')
    else:
        print(f'{osoba1} >  {osoba2}')


o1 = Osoba('Jan', 'Kowalski', True, 1980)
o2 = Osoba('Adam', 'Nowak', True, 1999)
o3 = Osoba('Dariusz', 'Kowalski', True, 1977)
o4 = Osoba('Jan', 'Jabłoński', True, 2001)
o5 = Osoba('Jan', 'Kowalski', True, 1974)

porownaj(o1, o2)
porownaj(o1, o3)
porownaj(o1, o4)
porownaj(o1, o5)
