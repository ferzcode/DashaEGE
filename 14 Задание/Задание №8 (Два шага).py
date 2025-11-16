maxi  = 399
for x in range(70000, 10, -1):
    num = 5 ** 2025 + 5 ** 400 - x
    c4 = 0
    while num > 0:
        if num % 5 == 4:
            c4 += 1
        num //= 5

    if c4 == maxi:
        print(x)
        break
    # maxi = max(maxi, c4)
# print(maxi)