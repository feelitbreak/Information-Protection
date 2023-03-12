# Лабораторная работа №2. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

sp_x = 0b0011_1000

x_n = 8

sp_key = 0b1101_1110_0101

key_n = 12

key_set1 = [1, 3, 5, 7, 2, 4, 6, 8]

key_set2 = [5, 7, 9, 11, 6, 8, 10, 12]

key_set3 = [12, 10, 4, 2, 1, 3, 9, 11]

s1 = [11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6]

s2 = [14, 7, 10, 12, 13, 1, 3, 9, 0, 2, 11, 4, 15, 8, 5, 6]

p_shift = 6


def get_key(main_key, key_set):
    str_main_key = f"{main_key:0{key_n}b}"
    res = []
    for x in key_set:
        res.append(str_main_key[x - 1])
    return int(''.join(res), 2)


def get_low_nibble(bin_num):
    return bin_num & 0b1111


def get_high_nibble(bin_num):
    return get_low_nibble(bin_num >> 4)


def concat_bin(bin_num1, bin_num2, n):
    return (bin_num1 << n) | bin_num2


def circular_shift_left(bin_num, d, n):
    return ((bin_num << d) % (1 << n)) | (bin_num >> (n - d))


def sp(x, key):
    cipher = (x + key) % 256
    t1 = get_high_nibble(cipher)
    t2 = get_low_nibble(cipher)
    n1 = s1[t1]
    n2 = s2[t2]
    cipher = concat_bin(n1, n2, x_n >> 1)
    return circular_shift_left(cipher, p_shift, x_n)


# main
if __name__ == "__main__":
    print("Task 1. SP-network.")

    key1 = get_key(sp_key, key_set1)
    print(f"Key 1: {key1:0{x_n}b}")
    y1 = sp(sp_x, key1)
    print(f"Interation 1 result: {y1:0{x_n}b}")

    key2 = get_key(sp_key, key_set2)
    print(f"Key 2: {key2:0{x_n}b}")
    y2 = sp(y1, key2)
    print(f"Interation 2 result: {y2:0{x_n}b}")

    key3 = get_key(sp_key, key_set3)
    print(f"Key 3: {key3:0{x_n}b}")
    y3 = sp(y2, key3)
    print(f"Interation 3 result: {y3:0{x_n}b}")
