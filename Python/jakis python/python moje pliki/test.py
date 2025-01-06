##print('hej właśnie zaczynam nauke pythona!!')
##owoc = 'pomidor'
##print (owoc)
zmienna1 = "hej to ja, \"to ja teraz mowie bla bla bla!\"    "
zmienna2 = 'hej to ja, moja ciocioa powiedziala "jaki piekny dzien:p"'
print(zmienna2)
print(zmienna1)
#tez tak można aby wyświetlil 3-cia litere ze stringu
owoc = 'pomarańcza z pomidorem'
print (owoc[2])
print(len(zmienna1), len(zmienna2))
zmienna3 = 'AUTOKAR'
zmienna4 = 'traktor'
print(zmienna4.upper())
print(zmienna3.lower())
print('ja ' +     'kali '        + 'lubieć '   + 'pomidory:)')
print('ja ' +     'krzysztof     '        + 'lubieć '   + '  pomidory:)')
print('co za fajny jezyk!!')
jeden = 'ja'
dwa = 'kocham'
trzy = 'jeść pieczone ziemniaki'
krzysztof = jeden + ' ' + dwa + ' ' + trzy + '.'
print(krzysztof)
print('* * ' *10)
zmienna5 = 'szczęście ' *12 # wyświetli 12 razy slowo szczęscie
print(zmienna5)
zmienna6 = 132
print('lubie frytki z ketchupem ' + str(zmienna6) + '.' )
print('ja {} smażone ziemniaki.' .format('lubie'))
print('{} {} {}' .format('ja', 'lubie', 'smażone ziemniaczki'))
print('ja {0} {1}. {1} {3} mnie.' .format('lubie', 'ziemniczki', 'mnie', 'lubią'))
#albo z formatem:)
print('   ')
print('{} {} {}.'.format(jeden, dwa, trzy))
print('{0:8}  |  {1:8}' .format('jabłko', 'gruszka'))
print('{0:8}  |  {1:8}' .format('jabłko', 3))
print('{0:8}  |  {1:8}' .format('gruszka', 13))
#mała zmiania
print('   ')
print('{0:8}  |  {1:<8}' .format('jabłko', 'gruszka'))
print('{0:8}  |  {1:<8}' .format('jabłko', 3))
print('{0:8}  |  {1:<8}' .format('gruszka', 13))
# teraz z > i może z ^
print('   ')
print('{0:8}  |  {1:^8}' .format('jabłko', 'pomarańcze'))
print('{0:8}  |  {1:^8}' .format('jabłko', 3))
print('{0:8}  |  {1:^8}' .format('gruszka', 13))
# jeszcze jedna
print('   ')
print('{0:8}  |  {1:>8}' .format('jabłko', 'pomarańcze'))
print('{0:8}  |  {1:>8}' .format('jabłko', 3))
print('{0:8}  |  {1:>8}' .format('gruszka', 13))
# float - wysiwelti do 2/3 miejsc po przecinku ale z dopelnieniem do zera
print('   ')
print('{0:8}  |  {1:<8}' .format('jabłko', 'pomarańcze'))
print('{0:8}  |  {1:<8.3f}' .format('jabłko', 3,1234354))
print('{0:8}  |  {1:<8.2f}' .format('gruszka', 1312,23))
# input dane np: input('podaje dane')
owoc = input('napisz jaki owoc lubisz: ')
print('{} to wspaniały owoc.' .format(owoc))
