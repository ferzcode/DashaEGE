from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 19: return f(n - 4) + 3580
    if n < 19: return 6 * (g(n - 7) - 36)


@lru_cache(None)
def g(n):
    if n >= 248045: return n / 20 + 28
    if n < 248045: return g(n + 9) - 4

for n in range(250000, 0, -1):
    g(n)

for n in range(0, 250000):
    f(n)


print(f(673))