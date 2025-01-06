from cw06_01.model.adres import Adres
from cw06_01.model.osoba import Osoba

print('początek deserializacji...')
with open('osoby.txt', 'r', encoding='utf-8') as plik:
    lista = list(map(eval, plik))
print('gotowe...')

print(*lista, sep='\n')
