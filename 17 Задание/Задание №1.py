a = [int(x) for x in open('17_25356.txt')]

chetire = [x for x in a if 1000 <= abs(x) <= 9999]
max30 = max([x for x in a if abs(x % 100) == 30])

c = 0
maxi = 0
res = []

for i in range(0, len(a) - 2):
    troyka = [a[i], a[i + 1], a[i + 2]]

    if troyka[0] not in chetire and troyka[1] not in chetire and troyka[2] not in chetire and sum(troyka) > max30:
        res.append(sum(troyka))

print(len(res), max(res))
        # c += 1
        # maxi = max(maxi, sum(troyka))
# print(c, maxi)