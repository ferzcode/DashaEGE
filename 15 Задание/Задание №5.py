def check(A):
    for dx in range(-1000, 1000):
        for dy in range(-1000, 1000):
            x = 38460 + dx
            y = 7692 + dy

            f = (x > A) or (5 * y > x) or (2 * x + 3 * y < 100001)
            if f == 0:
                return 0

    return 1


for A in range(38462, 10 ** 8, 1):
    if check(A) == 1:
        print(A)