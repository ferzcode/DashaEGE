for x in range(0, 37):
    number1 = 9 * 37 ** 4 + 8 * 37 ** 3 + x * 37 ** 2 + 3 * 37 ** 1 + 1 * 37 ** 0
    number2 = 1 * 37 ** 4 + x * 37 ** 3 + 9 * 37 ** 2 + 2 * 37 ** 1 + 4 * 37 ** 0

    if (number1 + number2) % 21 == 0:
        print((number1 + number2) // 21)