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


