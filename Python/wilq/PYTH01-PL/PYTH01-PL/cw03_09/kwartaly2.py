"""
skrypt przekształca krotkę miesięcy w nową listę w której miesiące są pogrupowane w kwartały
"""

# lista nazw miesięcy
rok = ('styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
       'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień')

liczba_kwartalow = 4
liczba_miesiecy = len(rok)
dlugosc_kwartalu = liczba_miesiecy // liczba_kwartalow

# lista kwartałów
# każdy kwartał jest listą 3 miesięcy
kwartaly = [[miesiac for nr_miesiaca, miesiac in enumerate(rok) if nr_miesiaca // dlugosc_kwartalu == numer_kwartalu]
            for numer_kwartalu in range(liczba_kwartalow)]

# wypisanie listy kwartałów
print('Kwartały:')
print(kwartaly, end='\n\n')

# wypisanie listy kwartałów, każdy kwartał w osobnej linii
print(*kwartaly, sep='\n')
