from cw06_01.osoby_test1 import osoby

print('początek serializacji...')
with open('osoby.txt', 'w', encoding='utf-8') as plik:
    for osoba in osoby:
        plik.write(f'{osoba!r}\n')  # konwersja osoba -> repr(osoba)

print('gotowe...')
