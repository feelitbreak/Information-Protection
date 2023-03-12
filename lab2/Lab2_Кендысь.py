# Лабораторная работа №2. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

sp_x = 0b0011_1000
sp_x_n = 8

sp_key = 0b1101_1110_0101
key_n = 12

key_set1 = [1, 3, 5, 7, 2, 4, 6, 8]
key_set2 = [5, 7, 9, 11, 6, 8, 10, 12]
key_set3 = [12, 10, 4, 2, 1, 3, 9, 11]

key_set_list = [key_set1, key_set2, key_set3]

s1 = [11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6]
s2 = [14, 7, 10, 12, 13, 1, 3, 9, 0, 2, 11, 4, 15, 8, 5, 6]

p_shift = 6

sp_iterations = 3

feistel_x = 0b0011_0001_0100_0110
feistel_x_n = 16

feistel_key = 0b1110_0100_1000

feistel_iterations = 6


def get_key(main_key, key_set):
    str_main_key = f"{main_key:0{key_n}b}"
    res = []
    for x in key_set:
        res.append(str_main_key[x - 1])
    return int(''.join(res), 2)


def get_low_half(bin_num, n):
    length = n >> 1
    return bin_num & ((1 << length) - 1)


def get_high_half(bin_num, n):
    length = n >> 1
    return bin_num >> length


def concat_bin(bin_num1, bin_num2, n):
    return (bin_num1 << n) | bin_num2


def circular_shift_left(bin_num, d, n):
    return ((bin_num << d) % (1 << n)) | (bin_num >> (n - d))


def sp(x, key):
    cipher = (x + key) % 256
    t1 = get_high_half(cipher, sp_x_n)
    t2 = get_low_half(cipher, sp_x_n)
    n1 = s1[t1]
    n2 = s2[t2]
    cipher = concat_bin(n1, n2, sp_x_n >> 1)
    return circular_shift_left(cipher, p_shift, sp_x_n)


def sp_output():
    print(f"Plaintext: {sp_x:0{sp_x_n}b}")
    y = 0
    for i in range(sp_iterations):
        key_i = get_key(sp_key, key_set_list[i])
        print(f"Key {i + 1}: {key_i:0{sp_x_n}b}")
        y = sp(sp_x, key_i)
        print(f"Interation {i + 1} result: {y:0{sp_x_n}b}")
    print(f"Encryption result: {y:0{sp_x_n}b}")


def feistel_iter(left, right, key):
    return right, left ^ sp(right, key)


def feistel_encrypt(x, key):
    left = get_high_half(x, feistel_x_n)
    right = get_low_half(x, feistel_x_n)
    for i in range(feistel_iterations):
        key_i = get_key(key, key_set_list[i % sp_iterations])
        left, right = feistel_iter(left, right, key_i)
    left, right = right, left
    return concat_bin(left, right, sp_x_n)


def feistel_output():
    print(f"Plaintext: {feistel_x:0{feistel_x_n}b}")
    cipher = feistel_encrypt(feistel_x, feistel_key)
    print(f"Encryption result: {cipher:0{feistel_x_n}b}")


# main
if __name__ == "__main__":
    print("Task 1. SP-network.")
    sp_output()

    print("Task 2. Feistel-network.")
    feistel_output()
