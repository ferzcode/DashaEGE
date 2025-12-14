nomer = 0

for stroka in open('9_23747.csv'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    tri = [x for x in s if s.count(x) == 3]
    solo = [x for x in s if s.count(x) == 1]

    if len(tri) == 3 and len(solo) == 4:
        if (sum(solo) / len(solo)) <= tri[0]:
            print(nomer, sum(s))