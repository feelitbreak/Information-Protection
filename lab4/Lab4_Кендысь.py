# Лабораторная работа №4. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

p = 1102914252601991
q = 571301412050021
n = p * q
e = 624840313709071966800768010501

x1 = 267222621555915275276288463243
y1 = 0

x2 = 0
y2 = 291064433434228628162063527294


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
        power /= 2

    return res


def get_d():
    phi = (p - 1) * (q - 1)
    res, unused, gcd = extended_euclidian(e, phi)

    if res < 0:
        res += phi

    if gcd == 1:
        print("Gcd = 1, so e is a public key.")
        return res
    else:
        print("e is not a public key.")
        return "Error"


# main
if __name__ == "__main__":
    print("Task 1. Private key d.")
    d = get_d()
    print(f"Private key d: {int(d)}.")
