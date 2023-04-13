# Лабораторная работа №5. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

import random
from hashlib import sha256

q = 204549505434169694705359613953840507945808782458714026455216935639206129681467
m = "I, Alexey Kendys, love MiKOZI"


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


def get_reverse(num, mod):
    res, unused, gcd = extended_euclidian(num, mod)

    if res < 0:
        res += mod

    return res


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
        in_r = random.randrange(2, 4 * (in_q + 1), 2)
        out_p = in_q * in_r + 1
        if fast_pow(2, in_q * in_r, out_p) == 1 and fast_pow(2, in_r, out_p) != 1:
            break

    while True:
        x = random.randrange(out_p)
        out_g = fast_pow(x, in_r, out_p)
        if out_g != 1:
            break

    out_d = random.randrange(in_q)
    out_e = fast_pow(out_g, out_d, out_p)

    return (out_p, in_q, out_g), out_e, out_d


def sign(in_p, in_q, in_g, in_d, in_m):
    h = sha256(in_m.encode("utf8"))
    m1 = int(h.hexdigest(), base=16)

    k = random.randrange(1, in_q)
    out_r = fast_pow(in_g, k, in_p)
    out_s = (get_reverse(k, in_q) * ((m1 - in_d * out_r) % in_q)) % in_q

    return out_r, out_s


def verify(in_p, in_q, in_g, in_e, in_m, in_r, in_s):
    if in_r >= in_p or in_r <= 0 or in_s >= in_q or in_s < 0:
        return False

    h = sha256(in_m.encode("utf8"))
    m1 = int(h.hexdigest(), base=16)

    if (fast_pow(in_e, in_r, in_p) * fast_pow(in_r, in_s, in_p)) % in_p == fast_pow(in_g, m1, in_p):
        return True
    else:
        return False


# main
if __name__ == "__main__":
    (p, q, g), e, d = gen(q)
    r, s = sign(p, q, g, d, m)
    print(verify(p, q, g, e, m, r, s))
