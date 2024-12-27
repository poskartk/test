# łanuchy znakow
# zmiennie typu string
# wiele z nich to wbudowane funkcje

# upper - zmienie znaki na wielkie
napis='ministerstwo długich kroków'
print(napis.upper())

# lower - zmieni znaki na male
napis='A TERAZ ZMIENI NA MAŁE LITERKI'
print(napis.lower())

# tile - powieksza pierwsze litery wszytkich wyrazow w ciagu
napis="to jest jakis napis, zmieni go na cos takiego:"
print(napis.title())
#wynik:
# To Jest Jakis Napis, Zmieni Go Na Cos Takiego:

#replace - podmieni znaki lub ciagi na inne
napis='ALA MA KOTA'
print(napis.replace("A","X"))
# wynik
# XLX MX KOTX

# len - pokaze ilosc znakow w stringu, nie jest to funkcja
x=len("to jest test i przykladowy tekst")
print(x)

# count - zliczy ilosc wystapien ciagu lub znaku w lancuchu tekstowym
napis="ALA MA KOTA I KOT MA ALE LA LA"
print(napis.count("LA"))
# wyswietli 3 bo jest 3 x LA

# strip - usuwa biale znaki, lub wskazane znaki w ciagu
napis='     ALA MA KOTA'
print(napis.strip())
# pokaze: ALA MA KOTA bez spacji

napis='ALA MA KOTA ALA'
print(napis.strip("ALA"))
# pokaze: MA KOTA -> bo wytnie ALA na poczatku/koncu tekstu

# split i join - zmiana tekstu na liste i listy na tekst
# dzieli lancuchy tekstowe na czesci
napis="to jest tekst"
print(napis.split())
# wynik:  ['to', 'jest', 'tekst'] -> to jest lista
# ale mozesz ja oddzielic srednikami np:
napis="LUBIE JESC MIOD"
print(napis.split(";"))
# wynik: ['LUBIE JESC MIOD'] // dziwne nie wiem czemu nie pokazal ;

# Łancuchy funkcji

napis="to ja Krzysztof Rafał Tomasz Poskart"
print(napis.strip("to").title().replace('Poskart','Bakoma'))
# pokaze:  Ja Krzysztof Rafał Tomasz Poskar

