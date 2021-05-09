import math


def kor_kerulet(r: float):
    return 2*r*math.pi


def kor_terulet(r: float):
    return math.pi*r**2


print("Egy kör területének és kerületének kiszámítása")
print("-----------------------------------------------")
r = float(input("Adja meg a sugár hosszát: "))
if r > 0:
    print("A kör kerülete = ", kor_kerulet(r))
    print("A kör területe = ", kor_terulet(r))
else:
    print("Hibás adat! Ilyen kört nem lehet szerkeszteni!")
    print("Próbálkozzon mással!")
