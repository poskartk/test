from cw03_A.utils import execute

print('W razie nieznalezienia: find zwraca -1, zaś index rzuca wyjątkiem')

commands = [
    "'blablabla'.find('la')",
    "'blablabla'.find('la', 6)",
    "'blablabla'.find('la', 2, 5)"
]
execute(commands, globals(), 'Zwracany jest najmniejszy indeks...')

commands = [
    "'blablabla'.rfind('bla')",
    "'blablabla'.rfind('bla', 7)",
    "'blablabla'.rfind('bla', 2, 6)"
]
execute(commands, globals(), 'Zwracany jest największy indeks...')
