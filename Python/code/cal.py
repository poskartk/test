# To jest mój I-szy program - kalkulator
powitanie="Witaj w moim programie"
print(powitanie.upper())

print("podaj liczbe a")
a = input()
print("podaj liczbe b")
b = input()
print("podane liczby to:",a,b)
suma == a+b
roznica == a-b
iloczyn == a*b
iloraz == a//b
print("Co chcesz zrobic? suma - 1 roznica - 2 iloczyn - 3 iloraz - 4")
decyzja = input()
if decyzja == 1:
    print("suma to:",suma)
elif decyzja == 2:
    print("roznica to:",roznica)
elif decyzja == 3:
    print("iloczyn to:",iloczyn)
elif decyzja == 4:
    print("iloraz to:",iloraz)
else:
    print('po temacie')