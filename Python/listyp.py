# Zaawansowane elementy przetwarzania list i zbiorów

# W praktyce programisty często zdarza się sytuacja w której na podstawie zawartości jednej listy
# tworzysz inną listę, często filtrując na podstawie zawartości. Przyjrzyjmy się jak to można zrobić
# przy pomocy dotychczas znanych metod i porównajmy to z zastosowaniem list składanych.

liczby=[]
for x in range(1,21): liczby.append(x)
print(liczby)

# wynik to wygenerowanie listy z 20 elementami od 1 do 20
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# a ten wygeneruje liczby parzyste w piramidce
parzyste=[]
for i in liczby:
    if(i%2==0):
        parzyste.append(i)
    print(parzyste)

# tylko ze ten wysuetli tez parzysta ale w jednej linii a nie piramidce:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print('=======')
parzyste=[i for i in liczby if i%2==0]
print(parzyste)

# analiza tego co powyzej 
# 1. "parzyste=" - powstanie nowa lista o nazwie parzyste do której przypiszemy....
# 2. "[i for" - każdy element z listy pierwotnej trafia do docelowej bez żadnej modyfikacji.
# 3. "i in liczby" - przetwarzamy elementy z listy "liczby" i do każdego z nich odnosimy się per "i"
# 4. "if i%2==0]" - do docelowej listy trafiają tylko liczby parzyste-czyli podzielne przez 2 bez reszty

print('=======')
# a to wysietli liczby ale pomoznone x10
parzyste=[i*10 for i in liczby]
print(parzyste)

print('psikus')

liczby=[]
for x in range(1,21): liczby.append(x)
print(liczby)
parzyste=[i*10 for i in liczby if i%2==0]
print(parzyste)
# wynik:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

# teraz zamiast dwoch list mozna jedna uzyc

print( [i for i in range(1,21) if i%2==0] )
# wynik: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]