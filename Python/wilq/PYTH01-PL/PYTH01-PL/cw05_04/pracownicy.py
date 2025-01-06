class Pracownik:
    def __init__(self, imie, nazwisko, zarobki):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__zarobki = zarobki

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.__imie} {self.__nazwisko}, zarobki: {self.__zarobki}'


class KierownikZespolu(Pracownik):
    def __init__(self, imie, nazwisko, zarobki, odpowiedzialnosc):
        super().__init__(imie, nazwisko, zarobki)
        self.__lista_pracownikow = []
        self.__odpowiedzialnosc = odpowiedzialnosc

    def dodaj_pracownika(self, pracownik):
        self.__lista_pracownikow.append(pracownik)

    def usun_pracownika(self, pracownik):
        if pracownik in self.__lista_pracownikow:
            self.__lista_pracownikow.remove(pracownik)

    def kto_w_zespole(self):
        return self.__lista_pracownikow

    def __str__(self):
        return super().__str__() + f', odpowiedzialność: {self.__odpowiedzialnosc}'


p1 = Pracownik('Jan', 'Kowalski', 4_000)
p2 = Pracownik('Tomasz', 'Jabłoński', 4_000)
kz1 = KierownikZespolu('Adam', 'Nowak', 6_000, 'projekt w Pythonie')
kz1.dodaj_pracownika(p2)

print(p1)
print(p2)
print(kz1)
print('Zespół:', *kz1.kto_w_zespole(), sep='\n')
