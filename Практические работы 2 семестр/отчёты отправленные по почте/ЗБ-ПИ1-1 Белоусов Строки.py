from collections import OrderedDict
import string


# Задание 1
# Реализовать одно алфавитный шифр Цезаря для шифрования и дешифрование строки любой длины
# и заданным ключем (сдвигом алфавита), используется кириллический алфавит,
# знаки препинания, цифры, верхний и нижний регистр.
def toCesar(str, k):
    alphabetUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabetLower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    k %= len(alphabetUp)

    for char in str:
        i = alphabetUp.find(char)
        if i != -1:
            result += alphabetUp[(i + k) % len(alphabetUp)];
            continue
        i = alphabetLower.find(char)
        if i != -1:
            result += alphabetLower[(i + k) % len(alphabetLower)];
            continue
        result += char

    return result


def fromCesar(str, k):
    lenalpha = 33
    return toCesar(str, lenalpha - k % lenalpha)


# Задание 2
# Реализовать шифр с использованием кодового слова,
# используется латинский алфавит с верхним регистром.
def toCode(str, codeword):
    alphabet = string.ascii_uppercase
    secretalpha = list(OrderedDict.fromkeys(codeword.upper() + alphabet).keys())
    result = ""

    for char in str:
        i = alphabet.find(char)
        if i != -1:
            result += secretalpha[i]
            continue
        result += char

    return result


def fromCode(str, codeword):
    alphabet = ''.join(list(OrderedDict.fromkeys(codeword.upper() + string.ascii_uppercase).keys()))
    secretalpha = string.ascii_uppercase
    result = ""

    for char in str:
        i = alphabet.find(char)
        if i != -1:
            result += secretalpha[i]
            continue
        result += char

    return result


# задание 3
# Реализовать двух алфавитный шифр Цезаря для шифрования и
# дешифрование строки любой длины и заданным ключем,
# используется латинский алфавит и цифры, а так же только нижний регистр.
def toDoubleCesar(str, k1, k2):
    alphabet = string.ascii_lowercase + string.digits
    result = ""
    k1 %= len(alphabet)
    k2 %= len(alphabet)

    for i in range(len(str)):
        char = str[i]
        index = alphabet.find(char)
        if index != -1:
            result += alphabet[(index + (k1, k2)[i % 2]) % len(alphabet)];
            continue
        index = alphabet.find(char)
        if index != -1:
            result += alphabet[(index + (k1, k2)[i % 2]) % len(alphabet)];
            continue
        result += char

    return result


def fromDoubleCesar(str, k1, k2):
    lenalpha = len(string.ascii_lowercase + string.digits)
    return toDoubleCesar(str, lenalpha - k1 % lenalpha, lenalpha - k2 % lenalpha)


# задание №4
# Реализовать шифр Виженера, который состоит из последовательности нескольких шифров Цезаря
# с различными значениями сдвига. Для зашифровывания может использоваться таблица алфавитов,
# называемая tabula recta или квадрат (таблица) Виженера.
# Строка для шифрования должна быть на основе латинского алфавита,
# ключевое слово вводится с клавиатуры.
def toVigenere(str, keyword):
    # alphabetUp = string.ascii_uppercase
    # alphabetLower = string.ascii_lowercase
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    result = ""
    # k %= len(alphabetUp)
    if any(alphabet.find(char) == -1 for char in keyword):
        raise ValueError("В ключе содержаться недопустимые символы")

    for i in range(len(str)):
        char = str[i]
        keyIndex = alphabet.find(keyword[i % len(keyword)])
        charIndex = alphabet.find(char)
        if charIndex != -1:
            result += alphabet[(charIndex + keyIndex) % len(alphabet)];
            continue
        result += char

    return result


def fromVigenere(str, keyword):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    result = ""

    if any(alphabet.find(char) == -1 for char in keyword):
        raise ValueError("В ключе содержаться недопустимые символы")

    for i in range(len(str)):
        char = str[i]
        keyIndex = alphabet.find(keyword[i % len(keyword)])
        charIndex = alphabet.find(char)
        if charIndex != -1:
            result += alphabet[(charIndex - keyIndex + len(alphabet)) % len(alphabet)];
            continue
        result += char

    return result


def main():
    print("Задание №1")
    print(toCesar("Hello world!Кодовое слово!АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, абвгдеёжзийклмнопрстуфхцчшщъыьэюя?!", 1))
    print(fromCesar("Hello world!Лпепгпё тмпгп!БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА, бвгдеёжзийклмнопрстуфхцчшщъыьэюяа?!", 1))
    print(toCesar("Hello world!Кодовое слово!АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, абвгдеёжзийклмнопрстуфхцчшщъыьэюя?!", 49))
    print(fromCesar("Hello world!Ъюуюсюф быюсю!ПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНО, прстуфхцчшщъыьэюяабвгдеёжзийклмно?!", 49))
    print()

    print("Задание №2")
    print(toCode("Hello world ".upper() + string.ascii_uppercase, "Hello"))
    print(fromCode("DAJJN WNRJO HELOABCDFGIJKMNPQRSTUVWXYZ", "Hello"))
    print()

    print("Задание №3")
    print(toDoubleCesar("Hello world!" + string.ascii_lowercase + string.digits + "?!", 1, 3))
    print(fromDoubleCesar("Hhmop xrsoe!bedgfihkjmlonqpsrutwvyx0z21436587a9c?!", 1, 3))
    print(toDoubleCesar("Hello world!" + string.ascii_lowercase + string.digits + "?!", 49, 27))
    print(fromDoubleCesar("H5yc1 9f4cq!n2p4r6t8vaxcze1g3i5k7m9obqdsfuhwjyl0?!", 49, 27))
    print()

    print("Задание №4")
    print(toVigenere("ATTACKATDAWN", "LEMON"))
    print(fromVigenere("LXfOPVEfRNhR", "LEMON"))
    print(toVigenere("ATTACK AT DAWN!", "LEMON"))
    print(fromVigenere("LXfOPV Mh OEib!", "LEMON"))
    try:
        print(toVigenere("ATTACK AT DAWN!", "ЛИМОН"))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
