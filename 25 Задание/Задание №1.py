from math import *

def f(n):
    d = []

    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return d # ДЛЯ ПРОСТОГО ЧИСЛА - RETURN []


c = 0
for n in range(1_324_728, 2_000_000):
    deliteli = f(n) # ВСЕ ДЕЛИТЕЛИ
    prostie = [d for d in deliteli if len(f(d)) == 0 and str(d).count('5') == 1]

    if len(prostie) == 2 and prod(prostie) == n and c < 5:
        print(n, max(prostie))
        c += 1