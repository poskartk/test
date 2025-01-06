"""
#### to jest OK ale chaszuje to narazie
def rowne_lub_różne(numer):
    if numer % 2 == 0:
        return 'parzysty'
    else:
        return 'nieparzysty'

#wywołanie tej funkcji z liczna 10 aby sprawdzil
jakiś_string = rowne_lub_różne(10)
print(jakiś_string)
"""

def podajliczbe():
    liczba = input('podaj liczbę: ')
    return liczba
    print('twoja liczta to: ')
    print(liczba)
    
def podajimie():
    imie = input('jak masz na imie: ')
    return imie
    print ('masz na imie: ')
    print(imie)
    
def czyparzyste(numer):
    if numer % 2 == 0:
        return 'parzysta liczba'
    else:
        return 'nieparzysta liczba'
print(czyparzyste(7))

podajimie()
podajliczbe()
czyparzyste(liczba)
