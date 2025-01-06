for nazwa_pliku in ('tekst_en.txt', 'tekst_pl.txt'):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        for linia in plik:                 # plik jest iterowalny, odczyt linia po linii
            print(linia.strip())
