nomer = 0
for stroka in open('9_23368.txt'):
    s = [int(x) for x in stroka.split()]
    nomer += 1

    if len(s) == len(set(s)):
        if (min(s) + max(s)) * 2 == (sum(s) - max(s) - min(s)) * 3:
            print(nomer)