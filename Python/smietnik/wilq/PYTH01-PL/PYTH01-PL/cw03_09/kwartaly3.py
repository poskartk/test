"""
Skrypt przekształca krotkę miesięcy w nową listę w której miesiące są pogrupowane w kwartały.
"""

# lista nazw miesięcy
rok = ('styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
       'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień')

liczba_kwartalow = 4
dlugosc_kwartalu = len(rok) // liczba_kwartalow

# lista kwartałów
# każdy kwartał jest listą 3 miesięcy
kwartaly = [rok[nr_kwartalu * dlugosc_kwartalu:(nr_kwartalu + 1) * dlugosc_kwartalu]
            for nr_kwartalu in range(liczba_kwartalow)]

# wypisanie listy kwartałów
print('Kwartały:')
print(kwartaly, end='\n\n')

# wypisanie listy kwartałów, każdy kwartał w osobnej linii
print(*kwartaly, sep='\n')
