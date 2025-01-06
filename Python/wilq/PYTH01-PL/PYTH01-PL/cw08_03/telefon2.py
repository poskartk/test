class BrakMinut(Exception):
    """
    Nasz własny wyjątek sygnalizujący brak wystarczającej liczby minut na karcie na rozmowę.
    """
    def __init__(self, pozostaly_czas):
        super().__init__(f'PROBLEM: Bieżąca rozmowa przekracza dozwolony limit {pozostaly_czas} min.')


class TelefonNaKarte:
    """
    Klasa symuluje działanie telefonu na kartę.

    atrybut __limit: przechowuje aktualny stan minut do wykorzystania
    """
    def __init__(self, starter):  # symulacja startera
        self.__minuty = starter

    def ile_minut(self):  # odczyt bieżącego stanu konta (ilości minut do wykorzystania)
        return self.__minuty

    def doladuj(self, dodatkowe_minuty):  # doładowanie konta
        self.__minuty += dodatkowe_minuty

    def rozmawiaj(self, czas_rozmowy):  # rozmowa
        if self.__minuty < czas_rozmowy:
            raise BrakMinut(self.__minuty)
        print('Fajnie się rozmawiało...', end=' ')
        self.__minuty -= czas_rozmowy


telefon = TelefonNaKarte(10)
for i in range(10):
    try:
        telefon.rozmawiaj(7)
    except BrakMinut as e:
        telefon.doladuj(5)
        print(f'{e} Doładowano kartę. Bieżący limit: {telefon.ile_minut()} min.')
    else:
        print(f'(na rozmowy pozostało {telefon.ile_minut()} min.)')
