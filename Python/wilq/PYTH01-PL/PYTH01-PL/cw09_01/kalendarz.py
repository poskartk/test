"""
Wieczny kalendarz.
"""
import datetime as dt

nazwa_dnia_tygodnia = 'niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota'

dzien = int(input('Podaj dzień: '))
miesiac = int(input('Podaj miesiąc: '))
rok = int(input('Podaj rok: '))

data = dt.date(rok, miesiac, dzien)
# isoweekday() zwraca: 1 - pon, 2 - wt, ..., 7 - nd
numer_dnia_tygodnia = data.isoweekday() % 7

print(data, 'to', nazwa_dnia_tygodnia[numer_dnia_tygodnia])
