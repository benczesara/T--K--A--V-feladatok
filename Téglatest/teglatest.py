

def teglatest_felszin(a: float, b: float, c: float):
    return 2 * ((a * b) + (a * c) + (b * c))


def teglatest_terfogat(a: float, b: float, c: float):
    return a * b * c


print("Egy téglatest felszínének és térfogatának kiszámítása")
print("------------------------------------------------------")
a = float(input("Adja meg az 'a' él hosszát: "))
b = float(input("Adja meg a 'b' él hosszát: "))
c = float(input("Adja meg a 'c' él hosszát: "))
if a > 0 and c > 0 and b > 0:
    print("A test felszíne = ", teglatest_felszin(a, b, c))
    print("A test térfogata = ", teglatest_terfogat(a, b, c))
else:
    print("Hibás adat! Ilyen téglatest nem létezik!")
