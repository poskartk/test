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
        print('Fajnie się rozmawiało...', end=' ')
        self.__minuty -= czas_rozmowy


# Test działania klasy
telefon = TelefonNaKarte(10)  # starter
for i in range(10):
    telefon.rozmawiaj(7)  # rozmowa

    # Doładowujemy konto mniejszą liczbą minut niż trwa rozmowa,
    # co może doprowadzić do braku środków, czyli sytuacji wyjątkowej.
    # Program nie jest na to przygotowany i zapewne doprowadzi
    # do ujemnego stanu konta... (będzie działał, tak jakby nic się nie stało)
    telefon.doladuj(5)  # doładowanie

    print(f'({telefon.ile_minut()} min pozostało a rozmowy)')  # ile minut pozostało?
