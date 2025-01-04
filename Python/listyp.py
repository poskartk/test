# Zaawansowane elementy przetwarzania list i zbiorów

# W praktyce programisty często zdarza się sytuacja w której na podstawie zawartości jednej listy
# tworzysz inną listę, często filtrując na podstawie zawartości. Przyjrzyjmy się jak to można zrobić
# przy pomocy dotychczas znanych metod i porównajmy to z zastosowaniem list składanych.

liczby=[]
for x in range(1,21): liczby.append(x)
print(liczby)

# wynik to wygenerowanie listy z 20 elementami od 1 do 20
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

parzyste=[]
for i in liczby:
    if(i%2==0):
    parzyste.append(i)
    print(parzyste)

