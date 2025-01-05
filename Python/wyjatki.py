# WYJATKI

# Dotychczas w wielu sytuacjach spotykaliśmy się z wyjątkami. Przy próbie dzielenia przez zero,
# przy próbie dostępu do nieistniejącego elementu słownika czy listy. W przypadku pojawienia się
# wyjątku program przestaje być wykonywany, dlatego warto reagować na pojawiające się wyjątki.

# cos aby powstal wyjatek - dzielenie przez zero:

print(1/0)
print("dalej")

# Słowo "dalej" nie zostało wypisane na konsoli, czyli program został przerwany w momencie
# pojawienia się wyjątku. Co jednak gdy chcielibyśmy aby w przypadku pojawienia się wyjątku
# został on obsłużony przez zaplanowany przez nas sposób, a program kontynuował swoje działanie?
# Tu z pomocą przychodzi nam konstrukcja try-except-finally-else dostępna w Pythonie.

try:
    print(1/0)
except:
    print("nie zabanglało")
print("dalej")
# Tym razem na konsoli nie pojawił się żaden wyjątek, za to zostało wydrukowane słowo "dalej".
# Powiedzieliśmy Pythonowi "try" - czyli spróbuj zrobić to, a jak się nie uda "except" to zrób to.
# Wyjątek pojawiający się w instrukcji "print(1/0)" został przechwycony w bloku except i została
# wykonana zaplanowana przez nas reakcja sprowadzająca się do wyświetlenia stosownego
# komunikatu. Ponieważ wyjątek został obsłużony program pracował dalej i na konsoli wyświetliło
# się również "dalej". Gdyby po instrukcji "print(1/0)" znalazły się jeszcze kolejne, nie zostałyby one
# wykonane.

# tylko mnie cos dalej wali z info ze ZeroDivisionError: division by zero

# Prezentowany kod będzie działał dla każdego wyjątku. Możemy także obsługiwać wskazane
# rodzaje wyjątków:
try:
    print(1/0)
except ZeroDivisionError:
    print("nie można dzielić przez zero!")

# Tym razem obsłużyliśmy jedynie wyjątego dzielenia przez zero (ZeroDivisionError). Gdyby kod
# spowodował pojawienie się innego wyjątku, nie zostałby on obsłużony. Na taką ewentualność też
# mamy sposób:
try:
    print(1/0)
except ZeroDivisionError:
    print("nie można dzielić przez zero!")
except:
    print("jakiś inny błąd")

# Inny błąd zostanie obsłużony instrukcjami pojawiającymi się po drugim wystąpieniu klauzuli
# "except". To byłaby taka obsługa ogólna dla wszystkich pozostałych wyjątków, którą musimy
# umieścić zawsze na końcu. Obługiwać wyjątki możemy też zbiorczo dla kilku wybranych rodzajów
# wyjątów:
try:
    print(1/0)
except(ZeroDivisionError,IOError):
    print("albo to, albo to")

# W powyższym przykładzie dla obu wyjątków obsługa sprowadzałaby się do tych samych
# czynności. Możemy też zechcieć odebrać komunikat błędu (np. żeby zarejestrować go w logach), a w takim
# przypadku nadajemy alias:
try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)

# tu pokazal faktycznie info ZeroDivisionError: division by zero

# Może się też tak zdarzyć że będziemy chcieli wykonać jakąś czynność niezależnie od wystąpienia
# lub nie wyjątku. Wtedy wykorzystujemy klauzulę finally:

try:
    print(1/0)
except:
    print("wyjątek")
finally:
    print("co by się nie działo to ja się uruchamiam")

# Istnieje też możliwość zareagowania w sytuacji gdy wyjątek nie wystąpił:

try:
    print("info")
except ValueError:
    print("wyjątek")
else:
    print("nie bylo wyjatku")

# Python umożliwia też wywoływanie wyjątków, nawet jeśli taki wyjątek nie wystąpi "naturalnie":
try:
    raise TypeError()
except TypeError:
    print("to było do przewidzenia...")
