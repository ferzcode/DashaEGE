for N in range(10000, 100000):
    k = str(N)
    S = sum(map(int, k)) # Сумма цифр
    M = int(max(i for i in k)) + int(min(i for i in k))

    L = int(k[0])
    R = int(k[-1])

    P1 = S - L
    P2 = M - R

    Z = str(min(P1, P2)) + str(max(P1, P2))

    if Z == '222':
        print(N)