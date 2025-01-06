# from pakiet import modul
from cw06_01.model import adres as a, osoba

osoby = [
    osoba.Osoba('Jan',
                'Kowalski',
                a.Adres('ul. Morska 11', '12-345', 'Gdańsk')),
    osoba.Osoba('Adam',
                'Bednarek',
                a.Adres('ul. Polna 3', '23-456', 'Mrągowo')),
    osoba.Osoba('Anna',
                'Jabłońska',
                a.Adres('ul. Polska 42', '34-567', 'Kołobrzeg'))
]

if __name__ == '__main__':
    print(*osoby, sep='\n')
