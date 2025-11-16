for x in range(1, 2031):
    num = 3 ** 100 - x

    c0 = 0
    while num > 0:
        if num % 3 == 0:
            c0 += 1
        num //= 3

    if c0 == 5:
        print(x)