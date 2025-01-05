# # Słowniki są zbiorem składającym się z klucza i wartości powiązanej z tym kluczem. Mogą spełniać
# taką samą rolę jak słowniki w bazach danych. Przypuśćmy że w hurtownii produktów AGD-RTV
# mamy wiele produktów wielu marek i wielu rodzajów. Na każdym z produktów znajduje się
# naklejka z kodem typu "AMICA561", które wykorzystujemy do odnalezienia szerszych informacji
# o produkcie. Oczywiście pod danym kluczem/kodem mogą znajdować się informacje tylko o
# jednym produkcie. Dwa produkty nie mogą posiadać tego samego kodu. W podobny sposób
# działają słowniki w Pythonie. Zwykle korzystając z klucza będziemy wyszukiwać wartość.
# Słowniki podobnie jak listy (i przeciwnie do krotek) są modyfikowalne.

# przyklad tworzenie pustych slownikow - jest ich kilka wariantow

slownik={}
slownik2=dict()

# przyklad zaplenionego slownika:
info={
"LG123": "Telewizor 60' z HD Ready, wejściem na internety i filtrem reklam",
"SONY666": "Piekielnie dobry telewizor",
"SZAJSUNG999": "Telewizor świetnie nadający się do zakrycia dziury w ścianie (i niczego więcej)"
}

# Wartości "LG123", "SONY666", "SZAJSUNG999" są w powyższym słowniku kluczami i to
# właśnie z nich korzystając będziemy wyszukiwali wartości. Wartości znajdują się po prawej stronie
# każdej wartości klucza po znaku ":". Kluczem mogą być nie tylko ciągi tekstowe, ale również
# liczby czy typy złożone. Podobnie rzecz ma się z wartościami

# Pobieranie warotsci ze slownikow

print(  info["SONY666"])  # da wynik: Piekielnie dobry telewizor

# Po słownikach możemy iterować w podobny sposób jak po listach czy krotkach, z tą różnicą że
# tutaj iterator jest kluczem a nie wartością:

for i in info:
    print(info[i])
print('-----')
for k in info.keys():
    print(info[k])  

# dwa powyzsze fory dadza taki sam wynik:
# Telewizor 60' z HD Ready, wejściem na internety i filtrem reklam
# Piekielnie dobry telewizor
# Telewizor świetnie nadający się do zakrycia dziury w ścianie (i niczego więcej)

# "i" w tym przypadku reprezentuje kolejne klucze w ramach słownika. Przechodzimy po całej
# długości słownika i korzystając z kolejnych wartości klucza wywołujemy "info[i]", czyli pobieramy
# kolejne wartości na podstawie kolejnego klucza.
# W drugim przypadku skorzystałem z wbudowanej funkcji "keys" z której skorzystanie w takim
# kontekście da nam taki sam wynik jak poprzednie rozwiązanie.

# Słowniki posiadają też funkcję "values" która działa na podobnej zasadzie jak "keys", z tą różnicą że zamiast 
# listy kluczy zwraca listę wartości (po której również możemy iterować).

print(info.keys()) 
# da: dict_keys(['LG123', 'SONY666', 'SZAJSUNG999'])
# z kolei
print(info.values())
# da:
# dict_values(["Telewizor 60' z HD Ready, wejściem na internety i filtrem reklam", 'Piekielnie
# dobry telewizor', 'Telewizor świetnie nadający się do zakrycia dziury w ścianie (i niczego
# więcej)'])

# Podobnie jak w listach czy krotkach, możemy analogiczną konstrukcją sprawdzić czy obiekt
# znajduje się na liście:

if "LG123" in info:
    print("Mamy taki produkt")
else:
    print("niet :(")  # pokaze Mamy taki produkt

# W podobny sposób możemy przeszukać wartości zamiast kluczy, i tu właśnie skorzystamy z funkcji
# "values":

if "Telewizor 60' z HD Ready, wejściem na internety i filtrem reklam" in info.values():
    print("mamy produkt o takim opisie")
else:
    print("taki opis nie pasuje do żadnego produktu")

# Sprawdzana w "if" wartość musi jednak dokładnie odpowiadać wartości ze słownika. Zwracam na
# to uwagę ponieważ w przypadku omawianych wcześniej łańcuchów tekstowych konstrukcja typu
# "if 'wartość' in 'coś coś coś wartość' zwróciłaby True i mógłbyś się tym zasugerować.

# Dodajemy i nadpisujemy elementy słowników w taki sam sposób:
info["KLUCZ"]="WARTOŚĆ"

# Jeśli w słowniku nie będzie elementu o podanym kluczu to zostanie od dodany. Jeśli będzie,
# zostanie nadpisany.
# Kasowanie elementu ze słownika odbywa się w podobny sposób jak w krotkach czy listach, z tą
# różnicą że zamiast indeksu elementu podajemy jego klucz:

del info["LG123"]