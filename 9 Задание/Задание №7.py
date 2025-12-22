k = 0
for stroka in open('9_13865.txt'):
    s = [int(x) for x in stroka.split()]

    usl1 = len(s) == len(set(s)) # True / False | 1 / 0
    usl2 = (min(s) + max(s)) * 2 <= (sum(s) - max(s) - min(s)) * 3 # True / False | 1 / 0
    #   0      1
    if usl1 + usl2 == 1:
        k += 1
print(k)