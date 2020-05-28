from collections import OrderedDict
import string

# Задание 1
def toCesar(str, k):
    alphabetUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabetLower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
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
            continue;
        result +=char;

    return result;


def fromCesar(str, k):
    lenalpha = 33
    return toCesar(str, lenalpha - k%lenalpha)


# Задание 2
def toCode(str, codeword):
    alphabet = string.ascii_uppercase
    secretalpha = OrderedDict.fromkeys(codeword+string.ascii_uppercase).keys()
    result = ""

    for char in str:
        i = alphabet.find(char)
        if i != -1:
            result += secretalpha[i]
            continue
        result += char

    return result


def fromCode(str, codeword):
    pass

def main():
    print(toCesar("Hello world!АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, абвгдеёжзийклмнопрстуфхцчшщъыьэюя?!", 1))
    print(fromCesar("Hello world!БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА, бвгдеёжзийклмнопрстуфхцчшщъыьэюяа?!", 1))
    print(toCesar("Hello world!АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, абвгдеёжзийклмнопрстуфхцчшщъыьэюя?!", 49))
    print(fromCesar("Hello world!ПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНО, прстуфхцчшщъыьэюяабвгдеёжзийклмно?!", 49))
    print(OrderedDict.fromkeys("abcdefGGhgk").keys())


if __name__ == "__main__":
    main()
