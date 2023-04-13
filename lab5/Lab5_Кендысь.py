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


def input_int_value(value_name):
    print(f"{value_name} = ")
    value = input()

    return int(value)


def input_str_value(value_name):
    print(f"{value_name} = ")
    value = input()

    return value


def menu():
    while True:
        print("\nWhat do you want the program to do? Type Gen, Sign, Verify or Exit.")
        inquiry = input()
        if inquiry == 'Gen':
            print("Input q.")
            in_q = input_int_value("q")

            (in_p, in_q, in_g), in_e, in_d = gen(in_q)
            print("Output:")
            print(f"p = {in_p}\nq = {in_q}\ng = {in_g}\ne = {in_e}\nd = {in_d}")

        elif inquiry == 'Sign':
            print("Input p, q, g, d, M.")

            in_p = input_int_value("p")
            in_q = input_int_value("q")
            in_g = input_int_value("g")
            in_d = input_int_value("d")
            in_m = input_str_value("M")

            in_r, in_s = sign(in_p, in_q, in_g, in_d, in_m)
            print("Output:")
            print(f"r = {in_r}\ns = {in_s}")

        elif inquiry == 'Verify':
            print("Input p, q, g, e, M, r, s.")

            in_p = input_int_value("p")
            in_q = input_int_value("q")
            in_g = input_int_value("g")
            in_e = input_int_value("e")
            in_m = input_str_value("M")
            in_r = input_int_value("r")
            in_s = input_int_value("s")

            print("Output:")
            print(verify(in_p, in_q, in_g, in_e, in_m, in_r, in_s))

        elif inquiry == 'Exit':
            break
        else:
            print("Invalid input.")


# main
if __name__ == "__main__":
    print("Default case.")
    print(f"q = {q}")
    print(f"M = {m}")

    (p, q, g), e, d = gen(q)
    print("Gen output:")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"g = {g}")
    print(f"e = {e}")
    print(f"d = {d}")

    r, s = sign(p, q, g, d, m)
    print("Sign output:")
    print(f"r = {r}")
    print(f"s = {s}")

    print("Answer for default value q:")
    print(verify(p, q, g, e, m, r, s))

    menu()
