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

napis="toja krzysztof poskar"
print(napis.strip("to").title().replace("P","X"))
# pokaze:  Ja Krzysztof Rafał Tomasz Poskar

# iteracja po lancuchach tekstowych
nazwa="dupadupa123zglossie"
for i in nazwa:
    print(i)
# wyswietli dupadupa123zglossie w koluemnie po jednym znaku


# mnozenie tekstu - powtorzenie danej frazy wiele razy
kriszna= "rama "*5+" "+5*"hare"
print(kriszna)
# wyswietli:
# rama rama rama rama rama  hareharehareharehare

# sprawdzanie tekstu czy zawiera jakas fraze
if ("X" in "SpaceX"):
    print('ten ciag znakow zawiera X!')
# z racji ze zabiera to wyswietli to co jest w print
# zamiast X moze byc dowolna fraza nie tylko jeden znak

# taki smaczek z ksiazki

if("Python">"Java"):
    print("to chyba jasne :) Tu jest miejsce na hejt: ........")
else:
    print("coś się spsuło...")
#wyswietli: to chyba jasne :) Tu jest miejsce na hejt: ........
# bo jakbys alfabetycznie te slowa uporzadkowal to Python bedzie po Javie :)

# ciecie lancuchow tekstowych.

lancuch='123456789'
print(lancuch[2])
# pokaze 3 bo w pythonie liczy od zera, czyli nie pokaze 1 ani 2-ki
# bo 1 to zerom 2 to jeden i 3 na liscie to 2 w lancuchu
print(lancuch[-2])
# pokaze 8 bo to drugi znak od konca 

print(lancuch[2:5])
# pokaze zakres: 345  

print(lancuch[:5])
# pokaze Isze 5 znakow: 12345

print(lancuch[:-3])
# lub wytnie ciag bez ostatnich 3 znakow od konca czyli pokaze 123456

print(lancuch[0:6:2])
# lub przeskakiwac co jakis znak - co dwa znaki od zerowej pozycji do 7mego: 135

print(lancuch[0:len(lancuch):2])
# np wyciecie co drugi znak z calego tekstu da 13579

print(lancuch[::2])
# to samo co powyzej -> 13579 ale w krotszy sposob