# Funkcje przydadzą nam się wszędzie tam gdzie będziemy potrzebowali kodu wielokrotnego użytku.
# Funkcje mogą przyjmować parametry różnych typów, mogą też zwracać jakieś dane.

# deklaracja

def sayhi():
    print('Hello My Friend')
# mozesz to potem wiele razy uzyc
# np w dowolnym miekjscu w troim kodzie ja przywolujesz jak ponizej:

sayhi() # wyswietli Hello My Friend

# Należy tylko pamiętać że deklaracja funkcji musi znajdować się nad jej wywołaniem. Z tego
# powodu funkcje deklarujemy zwykle na początku pliku, lub w osobnym module (jeden z kolejnych
# tematów) który następnie importujemy na początku pliku.

# Parametry funkcji służą do przekazywania do niej danych.

def sayHello(imie):
    print("Hello my friend {}!".format(imie))

# Powyżej przeróbka poprzedniego przykładu. Nie możemy posiadać w tym samym pliku dwóch
# funkcji o tej samej nazwie a różniącej się tylko liczbą parametrów. Przeciążanie tu nie funkcjonuje.
# Każda kolejna funkcja o takiej samej nazwie przesłania poprzednią.


# Funkcje mogą przyjmować wiele parametrów, rozdzielamy je przecinkami:

def dodaj(x, y):
    print(x+y)

# Funkcje z parametrami wywołujemy tak samo jak te bez parametrów, z tym że musimy podać
# wartości które do parametrów mają trafić:

dodaj(33,445)  # po jej wywolaniu faktycznie doda te dwie wartosci

# Wartości parametrów można podmieniać wewnątrz funkcji - nie są tylko do odczytu jak w
# niektórych językach programowania. Przykładowo poniższa funkcja zawsze będzie witała
# Czesława, niezależnie od tego co podamy przy wywołaniu:

def sayHello(imie):
    imie="Czesław"
    print("Hello my friend {}!".format(imie))

# Ponieważ zdeklarowane przez nas funkcje mogą być użytkowane przez inne osoby, a te
# niekoniecznie będą wiedziały jaki rodzaj danych nasza funkcja obsługuje, warto znać sposób na
# sprawdzenie typu danych które zostają podane przez parametry:

def sprawdz_typ(x):
    if( isinstance(x,int)): # sposób na sprawdzenie czy parametr jest spodziewanego typu
        print('otrzymalem liczbe calkowita')
    else:
        print('otrzymalem cos innego niz liczba calkowita')


# W Pythonie możemy również zadeklarować wartość domyślną dla parametru funkcji:

def domyslne_wartosci(a="brak",b="brak"):
    print('a='+a)
    print('b='+b)

# i po jej wywolaniu:

domyslne_wartosci("X","Y")
domyslne_wartosci()
domyslne_wartosci("coś")
domyslne_wartosci(b="coś innego")

# bedziesz mial takie cos na consoli:

# a=X
# b=Y
# a=brak
# b=brak
# a=coś
# b=brak
# a=brak
# b=coś innego

# W pierwszym przypadku wywołanie jak dotychczas. Chciałem jedynie zaznaczyć, że fakt
# posiadania przez funkcję wartości domyślnych parametrów nie powoduje że nie możemy jej
# wywoływać tak jak we wcześniejszych przykładach.
# W drugim nie podaję wartości dla parametrów, a funkcja przyjmuje wartości domyślne.
# Trzeci wariant jest bardzo ciekawy - co jeśli podamy mniej wartości niż parametrów? Python
# przypisze je do parametrów wg. kolejności, a pozostałe przyjmą wartości domyślne - ale tylko jeśli
# takie wartości zostaną zadeklarowane. Bez tego dostalibyśmy wyjątek.
# Czwarta opcja to przekazywanie wartości do parametrów po nazwie.

# Zwracanie wynikow funkcji

# Funkcje mogą zwracać wartości. Mogą to być pojedyncze liczby czy ciągi tekstowe, ale również
# złożone struktury jak np. tablice. Najprostsza funkcja zwracająca "0":

def oddaj0():
    return 0

# Wynik z takiej funkcji możemy odebrać i przekazać do innej funkcji (np. print), albo przypisać do
# jakiejś zmiennej:

print(oddaj0())
x=oddaj0()
print(x)


def dajcyferki():
    l=list(range(10))
    return l

dajcyferki()