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
    