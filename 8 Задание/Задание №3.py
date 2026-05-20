from itertools import *


c = 0
for x in product('0123456789ABC', repeat=5):
    s = ''.join(x)

    if s[0] != '0' and s.count('0') == 1:
        k = 0
        for i in range(0, len(s) - 1):
            if s[i] != s[i + 1]:
                k += 1

        if k == 4:
            c += 1

print(c)