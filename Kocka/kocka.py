

def kocka_felszin(a: float):
    return 6 * a * a


def kocka_terfogat(a: float):
    return a * a * a


print("Egy kocka felszínének és térfogatának kiszámítása")
print("--------------------------------------------------")
a = float(input("Adja meg az él hosszát: "))
if a > 0:
    print("A kocka felszíne = ", kocka_felszin(a))
    print("A kocka térfogata = ", kocka_terfogat(a))
else:
    print("Hibás adat! Ilyen kocka nem létezik!")
