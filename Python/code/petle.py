
# petle do testowania

#jeden warunek:
wzrost=190
if(wzrost>180):
    print('kobiety lubią to ;)')
print('no i koniec...')

#kilka warunkow
wzrost=152
if(wzrost>190):
    print('lasi to luba ;)')
elif(wzrost>180):
    print('niezle ale to i tak dla mnie za nisko')
elif(wzrost>170):
    print("jestes za niski dla mnie")
elif(wzrost>150):
    print('jestes niski do USA marines mozesz isc')
else:
    print('no nic koniec testowania')
print('no i koniec')

#inny przyklad na laczenie warunkow

w=180
sal=10000
if(w>175 and sal>9000):
    print('jestes NOK nie dostaniesz powyzki')

#while - wykonuje sie non stop
#c=1
#while(c<=20):
#    print(c)

# petla for - tyle razy sie wykona ile okrelsimy przez zakres zmiennej

for i in range(1,12):
    print(i)
# wyswietli numery od 1 do 11 w kolumnie.

# a tutaj wyswietli co druga wartosc czyli 1,3,5,7,9,11
for i in range(1,12,2):
    print(i)

# a tutaj wysiwelti od 10 w dol czyli 10,9,8,7,6 itd do 1
for i in range(10,0,-1):
    print(i)

# zagnieźdzanie petli

for i in range(1,11):
    for ii in range(1,11):
        print('i={}, ii={}'.format(i,ii))
# wyswietli takie cos:
# y=1, x=1
# y=1, x=2
# y=1, x=3
# y=1, x=4
# .... az do 10 dla x i y

# ponizsze da taki sam wynik ale z petlami while

y,x=1,1
while(y<=10):
    x=1
    while(x<=10):
        print('y={}, x={}'.format(y, x))
        x+=1 # to samo co x=x+1
    y+=1

# break - do przerywania petli

for x in range(1,101):
    if(x%17.5==0):
        print("szukana liczba to {}".format(x))
        break
# Powyższy kod szuka pierwszej liczby z zakresu 1-100 podzielnej przez 17.5. Przeszukujemy zakres
# liczba po liczbie i sprawdzamy czy reszta z dzielenia tej liczby przez 17.5 wynosi 0. Jeśli tak, to jest
# to poszukiwana przez nas liczba i można przerwać dalsze poszukiwania z użyciem instrukcji break.

# intrukcja continue

for x in range(-10,11):
    if(x==0):
        continue
    print(1/x)

# drukuje wynik dzielenie 1 przez kolejne wartosci z zakresu -10,10.
# oczywiscie jakby trafilo na dzielenie przez 0 to by sie wykrzaczylo
# continue powoduje przeskok do dalszej instrukcji aby skryp sie wykonal
# to taki rodzaj bezpiecznika

