animals = ['kot', 'pies', 'świnia', 'pająk']
print(animals[1])
animals[0] = 'koń'
print(animals[0])
print(animals)
print(animals[-1])
print(animals[-2])
print(animals[-3])
print(animals[-4])
animals.append('kura') # doda jako ostatni wpis do tablicy kure
print(animals[-1])

#rozrzerzanie listy:)
animals.extend(['wąż', 'jaszczyrka', 'sarna'])
more_animals = ['tirex', 'brontozaur']
animals.extend(more_animals)
print(animals)

# albo można na dowolna pozycje wstawić coś do listy za dolara wstawi boliwara
# lub za euro wstawi jena
# poprostu dodaje we wskaanej pozycji wpis i przesuwa wzystko o jednen kursor
kasa = ['dolar', 'euro', 'złotówka']
kasa.insert(0, 'boliwar')
print(kasa)
kasa.insert(2, 'jen')
print(kasa)

# slices:)

kolory = ['niebieski', 'czerwony', 'żółty', 'różowy', 'lazurowy', 'lapisowy']
jakies_kolory = kolory[0:3] # jak = kolory[:3] to pierwsze 3 wyswietli
print('jakieś kolory: {}' .format(jakies_kolory))
jakies_kolory = kolory[4:5]
print('jakieś kolory: {}' .format(jakies_kolory))
jakies_kolory = kolory[-2:] # ostatnie dwa:)
print('jakieś kolory: {}' .format(jakies_kolory))


#możesz też poszczegolny znak wysiwrtlic, wyswietli "raz" ze stringu

jakaś_lista = 'kutasrazdwatrzy' [5:8]
print(jakaś_lista)

# szukanie itemu w liscie, - da wynik 5 bo warka jest na pozycji 5-tej;)
piwo = ['tyskie', 'eb', 'tyskie' ,'dr brew', 'lech', 'warka']
indeks_piwa = piwo.index('warka')
print(indeks_piwa)
#jak nie znajdzie da error value
