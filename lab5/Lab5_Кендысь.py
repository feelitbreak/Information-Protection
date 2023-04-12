# Лабораторная работа №5. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

import random

q = 204549505434169694705359613953840507945808782458714026455216935639206129681467


def extended_euclidian(a, b):
    if a == 0:
        return 0, 1, b

    prev_x, x = 1, 0
    prev_y, y = 0, 1

    while b != 0:
        div = a // b

        (x, prev_x) = (prev_x - (div * x), x)
        (y, prev_y) = (prev_y - (div * y), y)

        (a, b) = (b, a % b)

    return prev_x, prev_y, a


def fast_pow(num, power, mod):
    num %= mod
    res = 1

    while power > 0:
        if power % 2 == 1:
            res *= num
            res %= mod

        num *= num
        num %= mod
        power //= 2

    return res


def gen(in_q):
    while True:
        r = random.randrange(2, 4 * (in_q + 1), 2)
        in_p = in_q * r + 1
        if fast_pow(2, in_q * r, in_p) == 1 and fast_pow(2, r, in_p) != 1:
            break

    while True:
        x = random.randrange(in_p)
        in_g = fast_pow(x, r, in_p)
        if in_g != 1:
            break

    in_d = random.randrange(in_q)
    in_e = fast_pow(in_g, in_d, in_p)

    return (in_p, in_q, in_g), in_e, in_d


# main
if __name__ == "__main__":
    (p, q, g), e, d = gen(q)
