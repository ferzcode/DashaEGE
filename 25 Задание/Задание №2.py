def f(n):
    d = set()

    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d # ДЛЯ ПРОСТОГО ЧИСЛА - RETURN {}

c = 0
for num in range(5_400_001, 6_000_000):
    deliteli = f(num)
    prostie = [d for d in deliteli if len(f(d)) == 0]

    M = min(prostie) + max(prostie) if len(prostie) > 1 else 0
    if M > 60_000 and str(M) == str(M)[::-1] and c < 5:
        print(num, M)
        c += 1