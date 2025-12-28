a = [int(x) for x in open('17_24892.txt')]

max9 = max([x for x in a if x < 0 and 1000 <= abs(x) <= 9999 and abs(x) % 9 == 0])

res = []
for i in range(0, len(a) - 1):
    if ((a[i] < 0) + (a[i + 1] < 0)) == 1:
        if (a[i] + a[i + 1]) > max9:
            res.append(a[i] ** 2 + a[i + 1] ** 2)

print(len(res), min(res))