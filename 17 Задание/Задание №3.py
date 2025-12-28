a = [int(x) for x in open('17_23757.txt')]

dvuznach = [x for x in a if 10 <= x <= 99]
mindv = min(dvuznach)

res = []

for i in range(0, len(a) - 1):
    if ((a[i] in dvuznach) + (a[i + 1] in dvuznach)) == 1:
        if (a[i] + a[i + 1]) % mindv == 0:
            res.append(a[i] + a[i + 1])

print(len(res), max(res))
