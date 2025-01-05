# Zestawy
# Zestawy to takie specyficzne zbiory elementów bez powtórzeń. W zestawach żadna wartość nie
# może się powtórzyć dwa razy. Są użyteczne np. do usuwania duplikatów. Dodatkowo zestawy
# automatycznie się sortują.

# rozne metody tworzenia zestawow

z={}
z2=set()

# Możemy też stworzyć zestaw od razu zapełniając go danymi:

z3={1,3,2,1,5,1}
print(z3)

# Pisałem wcześniej że zestawy nie mogą zawierać duplikatów, a tymczasem dodałem kilkukrotnie tę
# samą wartość "1". Przy takiej deklaracji nie dostaniemy żadnego wyjątku. Po prostu "1" na liście
# wystąpi tylko raz. W dodatku dane będą posortowane. Sprawdźmy co zobaczymy na konsoli po
# uruchomieniu powyższego kodu:
# wynik:  {1, 2, 3, 5}

# a jak jest zestaw zlozony to: 

z4={(1,"A"),(2,"B"),(1,"C"),(1,"A")}
print(z4)

# wynik:
# {(1, 'A'), (1, 'C'), (2, 'B')}  -> tylko ten duplikat usunie (1,A) bo ma mają identyczną zawartość wszystkich
# podelementów

# Jeśli na przykład mamy zbiór elementów pod postacią listy lub krotki, a chcielibyśmy pozbyć się z
# nich duplikatów to jak to zrobić? Możemy do tego celu wykorzystać właśnie zestawy:

lista=[1,2,3,4,3,2,1]
zestaw=set(lista)
lista2=list(zestaw)
print(lista2)
# Powyższy kod drukuje na konsoli taki wynik:
# [1, 2, 3, 4]

#===Modyfikacja zestawow za pomoca add i remove.

s={1,1,1,2,3,4}
s.add(5)   # doda 5
s.remove(1) # usunie 1 - oraz jej wszytkie wystapienia bno to usuwa zawartosc 
print(s)
# wynik
# {2, 3, 4, 5}
