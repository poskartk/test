with open('calosc.txt', 'w', encoding='utf-8') as wyjscie:
    for nazwa_pliku in ('tekst_en.txt', 'tekst_pl.txt'):
        with open(nazwa_pliku, 'r', encoding='utf-8') as wejscie:
            wyjscie.write(wejscie.read())
            wyjscie.write('\n')
