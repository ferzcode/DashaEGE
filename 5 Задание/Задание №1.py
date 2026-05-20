def tri(N):
    new = ''
    while N > 0:
        new = str(N % 3) + new
        N = N // 3

    return new

a  = []
for N in range(1, 1000):
    b = tri(N)

    if N % 3 != 0:
        b = '1' + b + b[-3:]
    else:
        summa = sum(map(int, b)) * 8
        b = b + tri(summa)

    R = int(b, 3)
    if R < 1220:
        a.append(R)
print(max(a))

# 1239

# 1205