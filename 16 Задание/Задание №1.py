from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 10: return n
    if n >= 10: return 3 * n + f(n - 3)

for n in range(1, 6500):
    f(n)

print((f(6250) + 2 * f(6244)) / f(6238))