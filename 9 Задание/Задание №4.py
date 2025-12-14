c = 0
for stroka in open('9_19117.txt'):
    s = [int(x) for x in stroka.split()]

    dva = [x for x in s if s.count(x) == 2] # len == 2
    solo = [x for x in s if s.count(x) == 1] # len == 3

    chet = [x for x in s if x % 2 == 0]
    nechet = [x for x in s if x % 2 != 0]

    if (len(dva) == 2 and len(solo) == 3) or (len(chet) > 0 and len(nechet) > 0 and sum(chet) > sum(nechet)):
        c += 1
print(c)