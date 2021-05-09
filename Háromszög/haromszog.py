import math


def haromszog_terulet(a: float, b: float, c: float):
    return math.sqrt(((a + b + c) / 2) * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))


def haromszog_kerulet(a: float, b: float, c: float):
    return a+b+c


print("Egy háromszög területének és kerületének kiszámítása")
print("-----------------------------------------------------")
a = float(input("Adja meg az 'a' oldal hosszát: "))
b = float(input("Adja meg a 'b' oldal hosszát: "))
c = float(input("Adja meg a 'c' oldal hosszát: "))
if a < b + c and c < a + b and b < a + c:
    print("A háromszög területe = ", haromszog_terulet(a, b, c))
    print("A háromszög kerülete = ", haromszog_kerulet(a, b, c))
else:
    print("Hibás adat! Ilyen háromszög nem szerkeszthető!")
