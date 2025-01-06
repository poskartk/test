suma = 1 + 2
różnica = 100 - 23
iloczyn = 23 * 12
kwadrat = 2 ** 42
modulo = 3 % 2
print('suma: {}' .format(suma))
print('różnica: {}' .format(różnica))
print('iloczyn: {}' .format(iloczyn))
print('kwadrat: {}' .format(kwadrat))
print('modulo: {}' .format(modulo))
"""zadanie na if z boolean"""
age = 377
if age >= 35:
    print('no stary jestes i tak za stary')
elif age >= 30:
    print('no jeszcze mozesz')
else:
    print('nie jesteś jeszcze taki stary mozesz wiele')    
print('młoda dupa z ciebie')

# funkcja powiatnie
def powitanie():
    print('cześć stary, miło mi cię powitać:)')

print('   ')
powitanie()

# może być funkcja z parametrem zmiennym

def powitanie1(name):
    print('Hi {}' .format(name))
name = input('podaj imie:')

powitanie1

#albo z dwoma argumentam
def powitanie3(name1,name2):
    print('Hi {} {}!' .format(name1,name2))
print(' ')
powitanie3('joe', 'diana')



""" to teź jest komenatrz! tylko wielolinijkowy:p
print('podaj liczbę z zakresu od 1 do 10:')
liczba = input('liczba:')
kwadrat = liczba ** liczba
modulu = liczba % liczba
iloczyn = liczba * liczba
print('kwadrat twojej liczby to:')
print(kwadrat)
print('modulo twej liczby to:')
print(modulu)
print('iloczyn twojej liczby to:')
print(iloczyn)
"""
