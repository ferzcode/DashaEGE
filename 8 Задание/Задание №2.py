from itertools import *

for dlina in range(4, 8):
    nomer = 0
    for x in product(sorted('ТАРКИ'), repeat=dlina):
        s = ''.join(x)
        nomer += 1

        s = s.replace('А', '*').replace('И', '*')


        if nomer % 2 == 0 and s[0] in 'ТРК' and '***' in s and s.count('*') == 3:
            if nomer == 31314:
                print(dlina)
