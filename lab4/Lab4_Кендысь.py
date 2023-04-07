# Лабораторная работа №4. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

p = 1102914252601991
q = 571301412050021
n = p * q
e = 624840313709071966800768010501

x1 = 267222621555915275276288463243

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
        power //= 2

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


def encrypt(x):
    return fast_pow(x, e, n)


def decrypt(y):
    return fast_pow(y, d, n)


# main
if __name__ == "__main__":
    d = get_d()
    print(f"Private key d: {int(d)}.")

    y1 = encrypt(x1)
    verif_x1 = decrypt(y1)
    print(f"\nPlaintext X1: {int(x1)}.")
    print(f"Result of encryption, ciphertext Y1: {int(y1)}.")
    print(f"Result of decryption, plaintext X1: {int(verif_x1)}.")

    x2 = decrypt(y2)
    print(f"\nCiphertext Y2: {int(y2)}.")
    print(f"Result of decryption, plaintext X2: {int(x2)}.")
