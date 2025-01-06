# Funkcja "map" służy do stosowania funkcji na każdym z elementów listy. Poniższy kod powoduje
# przetworzenie listy "liczby" w taki sposób, by do listy "parzyste" trafiły wartości z listy "liczby"
# pomnożone przez 2.

liczby=[i for i in range(1,11)]
parzyste=list(map(lambda x:x*2,liczby))
print(parzyste)

# pokaze: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# elemtn list powoduje powstanie listy ale ciekawa jest lamnda

# map(lambda x:x*2,liczby) -> tutaj trafiaja dwa paramerty
# zapis x: - oznacza ze to dynamiczna funkcja 
# lambda x:x*2 jest to samo co nizej:

# def funkcja(x):
#     return x*2  -> czyli to jakby fukncja mnozenie x*x

# tak czy inaczej:
# parzyste=list(map(lambda x:x*2,liczby))
# jest to samo co to:
# parzyste=[i*2 for i in liczby]


# Funkcja filter jak sama nazwa wskazuje, służy do filtrowania zawartości list.

liczby=[i for i in range(1,21)]
parzyste=list(filter(lambda x: x%2==0 ,liczby))
print(parzyste)

# da: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# istotne jest to: parzyste=list(filter(lambda x: x%2==0 ,liczby))
# jest to samo co: parzyste=[x for x in liczby if x%2==0]
# Tym razem w wyrażeniu lambda oczekuje się od nas warunku logicznego stwierdzającego
# "prawda" lub "fałsz" dla każdego z filtrowanych elementów. Robi to fragment "x%2==0" dla
# którego jesteśmy w stanie stwierdzić dla każdego elementu czy podane wyrażenie będzie
# prawdziwe czy nie. Będzie prawdziwe oczywiście tylko dla liczb parzystych, więc tylko takie trafią
# do listy docelowej.


# KROTKI
# Krotki w zasadzie podobne są bardzo do list. Właściwie to krotka jest taką listą której zawartości
# nie można zmieniać, w związku z czym nie posiada np. funkcji sortowania czy odwracania które
# działają przecież bezpośrednio na zbiorze. Nie posiadają też np. funkcji insert czy append.
# Zawartość krotki deklarujemy przy jej definicji, potem nie możemy już jej zmienić.
# Skoro krotki są takimi ograniczonymi listami to właściwie po co nam one? Typ danych który po
# zaincjalizowaniu zmiennej jest "tylko do odczytu" może być czasami przydatny. Ponadto krotki
# działają szybciej niż listy, z tego też powodu wiele bardzo użytecznych funkcji z różnorakich
# bibliotek Pythona zwraca nam właśnie taki typ danych.

# krotki jak i listy maja dwa mozliwe warianty deklaracji:
# tylko zmiana nawiasow z [] na ():

krotka=("Tytanowy Janusz","Molibdenowy Mateusz",777,"Przypadkowy tekst",[12,55,"koza"])
krotka2=tuple()
print(krotka,krotka2)
# wynik: 
# ('Tytanowy Janusz', 'Molibdenowy Mateusz', 777, 'Przypadkowy tekst', [12, 55, 'koza']) ()



# pobieranie krotek

madness=("Longer","jeśli","to","czytasz i nie jesteś","lamus","to","podrzuć","jakiegoś","dobrego","mema") # definicja
print(madness[2:7]) # pokaze elementy od 2 do 7 z krotki
print('====')
print(madness[0:5:2])
print('-----------')
if "Longer" in madness:
    print("Wygrałem! :D")
for m in madness:
    print(m)