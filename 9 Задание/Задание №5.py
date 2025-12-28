nomer = 0
for stroka in open('9_24346.csv'):
    nomer += 1
    s = [int(x) for x in stroka.split()]

    odinochki = [x for x in s if s.count(x) == 1]
    povtorki = [x for x in s if s.count(x) > 1]

    sum_povtorki = sum(povtorki) ** 2
    sum_odinochki = sum(odinochki) ** 2

    if len(odinochki) > 0 and len(povtorki) > 0 and sum_povtorki > sum_odinochki and sum(s) % 2 != 0:
        print(nomer)


