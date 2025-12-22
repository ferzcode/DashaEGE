c = 0

for stroka in open('9_14253.txt'):
    s = [int(x) for x in stroka.split()]

    povtorki = [x for x in s if s.count(x) == 2] # len(povtorki) == 6
    odinochka = [x for x in s if s.count(x) == 1] # len(odinochka) == 1

    if (len(povtorki) == 6 and len(odinochka) == 1) or ((sum(s) / len(s)) ** 0.5 == int((sum(s) / len(s)) ** 0.5)):
        c += 1
print(c)

