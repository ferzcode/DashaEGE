a = [int(x) for x in open('17_29349.txt')]
otvet = []

min123 = min([x for x in a if abs(x) % 123 == 0 and x > 0])

for i in range(0, len(a) - 1):
    if (a[i] + a[i + 1]) < min123:
        otvet.append(a[i] + a[i + 1])

print(len(otvet))
print(abs(max(otvet)))