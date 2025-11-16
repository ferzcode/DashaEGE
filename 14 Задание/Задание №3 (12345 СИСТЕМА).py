for x in range(0, 36):
    number1 = 1 * 36 ** 4 + 2 * 36 ** 3 + x * 36 ** 2 + 4 * 36 ** 1 + 5 * 36 ** 0
    number2 = 1 * 12345 ** 1 + x * 12345 ** 0

    if (number1 + number2) % 13 == 0:
        print((number1 + number2) // 13)