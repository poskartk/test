with open('tekst_en.txt', 'r', encoding='utf-8') as plik1, \
        open('tekst_pl.txt', 'r', encoding='utf-8') as plik2:
    for linia1, linia2 in zip(plik1, plik2):
        print(linia1.strip())
        print(linia2.strip())
