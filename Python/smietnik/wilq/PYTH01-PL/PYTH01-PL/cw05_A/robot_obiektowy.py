class Robot:
    __liczba_dzialajacych = 0

    @classmethod
    def ile_dziala(cls):
        return cls.__liczba_dzialajacych

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.czy_wlaczony = False
        self.x = 0
        self.y = 0

    def wlacz(self):
        if self.czy_wlaczony:
            print(f'Robot {self.nazwa} został już wcześniej włączony')
        else:
            print(f'Robot {self.nazwa} został włączony')
            self.czy_wlaczony = True
            self.__class__.__liczba_dzialajacych += 1

    def wylacz(self):
        if self.czy_wlaczony:
            self.czy_wlaczony = False
            self.__class__.__liczba_dzialajacych -= 1
            print(f'Robot {self.nazwa} został wyłączony')
        else:
            print(f'Robot {self.nazwa} został już wcześniej wyłączony')

    def idz(self, kierunek, kroki):
        if self.czy_wlaczony:
            if kierunek == 'N':
                self.y += kroki
            elif kierunek == 'S':
                self.y -= kroki
            elif kierunek == 'E':
                self.x += kroki
            elif kierunek == 'W':
                self.x -= kroki
        else:
            print(f'Robot {self.nazwa} nie może się poruszyć, gdyż jest wyłączony...')

    def jaka_pozycja(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return f'Robot {self.nazwa} jest {"włączony" if self.czy_wlaczony else "wyłączony"} ' \
               f'i znajduje się w punkcie {self.jaka_pozycja()}'

    def __lshift__(self, other):
        print(f'Przeniesienie robota {other.nazwa} do pozycji robota {self.nazwa}')
        other.x = self.x
        other.y = self.y

    def __rshift__(self, other):
        if self.czy_wlaczony:
            print(f'Przeniesienie robota {self.nazwa} do pozycji robota {other.nazwa}')
            self.x = other.x
            self.y = other.y
        else:
            print(f'Robot {self.nazwa} nie może się przesunąć, gdyż jest wyłączony')

    def __neg__(self):
        r = Robot(self.nazwa)
        r.x = -self.x
        r.y = -self.y
        return r

    def __eq__(self, other):
        return self.nazwa == other.nazwa

    def __hash__(self):
        return hash(self.nazwa)


r1 = Robot('R2-D2')
r2 = Robot('C-3PO')
r3 = Robot('R2-D2')
print(r1 == r3)
s = {r1, r3}
print(len(s))
# print(Robot.ile_dziala())
# r1.wlacz()
# r1.idz('N', 7)
# r2.idz('E', 4)
# r2.wlacz()
# r2.idz('E', 4)
# r2.wylacz()
# print(r1)
# print(r2)
# r1 >> r2
# print(r1)
# print(r2)
# r1 = -r1
# print(r1)
