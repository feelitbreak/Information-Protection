# Лабораторная работа №1. Вариант 8. Кендысь Алексей

alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
    'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]


def get_num(letter):
    return alphabet.index(letter)


def get_letter(num):
    return alphabet[num]


def input_text_key():
    print("Input text to be encrypted.")
    in1 = input()
    print("Input key.")
    in2 = input()
    return in1, in2


def vigenere():
    ciphertext_list = []
    for i in range(len(plaintext)):
        num1 = get_num(plaintext[i])
        num2 = get_num(key[i % len(key)])
        num = (num1 + num2) % len(alphabet)
        ciphertext_list += get_letter(num)

    return ''.join(ciphertext_list)


# main
if __name__ == "__main__":
    print("Task 1. Encryption, Vigenere cipher.")
    plaintext, key = input_text_key()
    print("Ciphertext: " + vigenere())
