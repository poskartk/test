"""
Program oblicza stan lokaty na koncie przy stałym oprocentowaniu po upływie określonego czasu
"""

# pobranie danych wejściowych
# funkcja input zwraca wartość w postaci tekstu, więc konieczna jest konwersja na typy liczbowe

# algorytm:
# stan lokaty po 0 latach: s0 = lokata
# stan lokaty po 1 roku:   s1 = s0 * (1 + stopa / 100)
# stan lokaty po 2 latach: s2 = s1 * (1 + stopa / 100) = s0 * (1 + stopa / 100) ** 2
# stan lokaty po 3 latach: s3 = s2 * (1 + stopa / 100) = s0 * (1 + stopa / 100) ** 3
# itd...
# stan lokaty po n latach: sn = s0 * (1 + stopa / 100) ** n


lokata = int(input('Podaj wartość lokaty: '))
stopa = float(input('Podaj roczną stopę oprocentowania [%]: '))
okres = int(input('Podaj czas lokaty (w latach): '))

# obliczenia
stan_koncowy = lokata * (1 + stopa / 100) ** okres

# wypisanie wyniku
print('\nStan lokaty po upływie okresu oszczędzania:', round(stan_koncowy, 2))
