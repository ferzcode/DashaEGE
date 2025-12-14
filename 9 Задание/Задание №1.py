c = 0

for stroka in open('9_25348.csv'):
    s = [int(x) for x in stroka.split()]

    tri = [x for x in s if s.count(x) == 3]
    solo = [x for x in s if s.count(x) == 1]
    maxi = max(s)

    if len(tri) == 3 and len(solo) == 4:
        if s.count(maxi) == 1:
            c += 1
print(c)