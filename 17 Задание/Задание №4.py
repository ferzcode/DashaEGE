a = [int(x) for x in open('17_23952.txt')]

max93 = max([x for x in a if x % 100 == 93])
summ93 = 0
otvet = []
for i in range(0, len(a) - 1):
    pair = [a[i], a[i + 1]]

    if ((pair[0] > max93) + (pair[1] > max93)) == 1:
        if (str(pair[0])[0] == '9' or str(pair[1])[0] == '9'):
            otvet.append(sum(pair))

            if pair[0] > max93:
                summ93 += pair[0]
            if pair[1] > max93:
                summ93 += pair[1]

print(len(otvet))
print(summ93)