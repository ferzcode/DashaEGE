maxi = 73
for x in range(1, 2030):
    num = 7 ** 170 + 7 ** 100 - x

    c0 = 0
    while num > 0:
        if num % 7 == 0:
            c0 += 1
        num //= 7

    if c0 == maxi:
        print(x)

    # maxi = max(maxi, c0)
# print(maxi)