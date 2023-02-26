# Лабораторная работа №1. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
    'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]

default_key2 = 'чтаюшднысхфьуёэцвеклиъямзойгжщрбп'


def get_num(letter):
    return alphabet.index(letter)


def get_letter(num):
    return alphabet[num]


def input_text_key1():
    in1 = input('Input text to be encrypted: ')
    in2 = input('Input key: ')
    return in1.lower(), in2.lower()


def input_text_key2():
    in1 = input('Input ciphertext to be decrypted: ')
    in2 = input('Input key (if invalid, default is used): ')

    if len(in2) != len(alphabet):
        print('Invalid key. Using default key: ' + default_key2)
        in2 = default_key2

    return in1.lower(), in2.lower()


def vigenere():
    ciphertext_list = []
    for i in range(len(plaintext1)):
        if plaintext1[i] == ' ':
            ciphertext_list.append(' ')
        else:
            num1 = get_num(plaintext1[i])
            num2 = get_num(key1[i % len(key1)])
            num = (num1 + num2) % len(alphabet)
            ciphertext_list.append(get_letter(num))

    return ''.join(ciphertext_list)


def get_sigma():
    sigma = [[], []]
    for i in range(len(alphabet)):
        sigma[0].append(i)
        key_num = get_num(key2[i])
        sigma[1].append(key_num)

    return sigma


def substitution():
    sigma = get_sigma()
    ciphertext_list = []
    for letter in plaintext2:
        if letter == ' ':
            ciphertext_list.append(' ')
        else:
            num = get_num(letter)
            ind = sigma[1].index(num)
            cipher_num = sigma[0][ind]
            ciphertext_list += get_letter(cipher_num)

    return ''.join(ciphertext_list)


# main
if __name__ == "__main__":
    print("Task 1. Encryption, Vigenere cipher.")
    plaintext1, key1 = input_text_key1()
    print("Ciphertext: " + vigenere())
    print("Task 2. Decryption, simple substitution cipher.")
    plaintext2, key2 = input_text_key2()
    print("Decrypted text: " + substitution())
