# mozna je zadeklaorwac na 2 sposoby
# mozna je odwracac, sortowac latwo i szybko przeszukiwac

lista=[]
lista2=list()

# obie beda puste ale znacza to samo

lista3=[1,2,3,"baba jaga patrzy"]
lista4=["nie","toperz",123,lista3]

# listy moga zawierac elementy dowolnych rodzajow i typow

print(lista4)
# mozna je wyswietlac i to bedzie takie cos:
# ['nie', 'toperz', 123, [1, 2, 3, 'baba jaga patrzy']]

# pobieranie wartosci z listy

print(lista4[-2])  # pobierze druga wartosc od konca listy czyli 123
print(lista4[1])   # albo Iszy elemeent - nie zeorwy czyli toperz

print(lista4[1:3])  # pobierze drugi i trzeci element czyli ['toperz', 123]
print(lista4[1:-1]) # zadzaila podobnie jak wyzej czyli ['toperz', 123]

print(lista4[1:len(lista4)-1])  # to samo da co wyzej ale za pomca len ['toperz', 123]

print(lista4[:3])
# ['nie', 'toperz', 123] - wszytko do pozycji 3 wlacznie, czyli do indeksu 2
print(lista4[2:]) 
# [123, [1, 2, 3, 'baba jaga patrzy']] -podobnie do indeksu nuemr 2
print(lista4[:])
# ['nie', 'toperz', 123, [1, 2, 3, 'baba jaga patrzy']] - no a tutaj all z listy 4 pokaze

# irterowanie po listach

li = ["siala","baba","mak","ale nalozyli",23,"%","VAT :)"]
for i in li:
    print(i)

# wyswietli all z listy li w slupku
# i jest kolejny element z listy a nie znakiem z lancucha
print('===========')


for i in range(len(i)):
    print(li[i])
# zadziala podobnie jak powyzsza petla tez wysietali all z listy li w slupku

# sprawdzanie czy elemnt znajduje sie na liscie:

poszukiwani=["Michał Nowak","Adam Mazur", "Kumar Kanan"]
if ("Adam Polak" in poszukiwani):
    print("jest na liscie")
else:
    print("a jednak go nie ma")

# modyfikowanie zawartosci listy

lista=[1,2,3,4,5,6,7]
lista.append(8)        # append doda na koncu listy element 
print(lista)
lista.insert(0,"X")    # insert podstawi wskazana wartosc w miejsce 0 indeksu w liscie
print(lista)
lista[1]="Y"       
print(lista)

#wynik oztwisty
# [1, 2, 3, 4, 5, 6, 7, 8]
# ['X', 1, 2, 3, 4, 5, 6, 7, 8]
# ['X', 'Y', 2, 3, 4, 5, 6, 7, 8]
print('===========')

#kasowanie elementow z listy

lista=[1,0,2,0,3,0,4,0,5,0,6,0,7,0,3]
del lista[2]   # usuniecie 2gieo elementu czyli 2ki w tym przypadku
print(lista)
lista.remove(3)  # usunie tylko pierwsze wystapienie wartosci 3 z listy
print(lista)
del lista[0:4]  # skasuje elementy o indeksch 0-3 
print(lista)
lista.clear() # kasuje cala zawarosc listy 
print(lista)

# pokaze:
# [1, 0, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 3]
# [1, 0, 0, 0, 4, 0, 5, 0, 6, 0, 7, 0, 3]
# [4, 0, 5, 0, 6, 0, 7, 0, 3]
# []

# sortowanie i odwracanie list

cos=["pomidor","ogorek","kiwi","jajko","pasztet"]
cos.sort()
print(cos)
# posortuje alfabetycznie na takie cos:
# ['jajko', 'kiwi', 'ogorek', 'pasztet', 'pomidor']
# jak byly by licbzy to by posortowala take rosnaco liczby
# ale jak poalczysz liczy i slowa to tego nie posortuje!

# sortowanie na odwrot

pdk=["Ogórek","Pomidor","Ziemniak","Marchew"]
pdk.sort()
pdk.reverse()
print(pdk)
# posortuje tak: ['Ziemniak', 'Pomidor', 'Ogórek', 'Marchew']
# taki sam efekt da ponizsze z uzyciem reverse

pdk=["Ogórek","Pomidor","Ziemniak","Marchew"]
pdk.sort(reverse=True)
print(pdk)

# a jak masz rozne typu to np:

furki=[[3,"Renault"],[2,"Citroen"],[1,"Audi"],[4,"Zaporożec"]]
furki.sort()
print(furki)

# posortuje to po numerach bo to Isza wartosc:
# [[1, 'Audi'], [2, 'Citroen'], [3, 'Renault'], [4, 'Zaporożec']]

# a jak chcesz po markach aut posortowac to masz:

from operator import itemgetter  # tylko musisz ta funkcje zaimportowac!
furki=[[3,"Renault"],[2,"Citroen"],[1,"Audi"],[4,"Zaporożec"]]
furki.sort(key=itemgetter(1))
print(furki)
# wynik taki sam: 
# [[1, 'Audi'], [2, 'Citroen'], [3, 'Renault'], [4, 'Zaporożec']]

lista=[1,3,5,8,13,21,34,55,1,1,1,"Batman"]
print(len(lista))     # pokaze ile jest elementow w liscie w tym przypadku 12
print(lista.count(1))  # tu pokaze ile razy w liscie wystepuje 1ka czyli 4 razy 

lista=[1,3,5,8,13,21,34,55,1,1,1,"Batman"]
podlista=lista[2:7]
print(podlista)
kopia=lista.copy()
print(kopia)

# wynik
# [5, 8, 13, 21, 34]   --> pokaze elementy od 2 do 7 z listy
# [1, 3, 5, 8, 13, 21, 34, 55, 1, 1, 1, 'Batman']  -> kopiuje cala liste 

# tez moga byc funkcje agregujace czyli suma, max z listy albo minimum
fib=[1,3,5,8,13,21,34,55]
print( sum(fib) , max(fib), min(fib) )

# wynik
# 140 55 1

fib=[1,3,5,8,13,21,34,55]
print(      fib.index(13))  # -> pokaze element numer 4 z listy czyli liczbe 13

