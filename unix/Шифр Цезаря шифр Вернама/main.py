import string

# Задание 1
# Реализовать одно алфавитный шифр Цезаря для шифрования и дешифрование строки любой длины
# и заданным ключем (сдвигом алфавита), используется кириллический алфавит
def toCesar(str, k):
    alphabetUp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabetLower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    k %= len(alphabetUp)

    for char in str:
        i = alphabetUp.find(char)
        if i != -1:
            result += alphabetUp[(i + k) % len(alphabetUp)]
            continue
        i = alphabetLower.find(char)
        if i != -1:
            result += alphabetLower[(i + k) % len(alphabetLower)]
            continue
        result += char

    return result


def fromCesar(str, k):
    lenalpha = 33
    return toCesar(str, lenalpha - k % lenalpha)

def fromCesarAll(str):
    lenalpha = 33
    for i in range(lenalpha):
        # print(i+1)
        print(toCesar(str, lenalpha - i % lenalpha))

def toVernam(str, k):
    # повторять строку s до зданной длины m
    def rep(s, m):
        a, b = divmod(m, len(s))
        return s * a + s[:b]
    fullkey = rep(k,len(str))
    result = ''
    for i in range(len(str)):
        result+=chr(ord(str[i])^ord(fullkey[i]))

    return result
    # print(chr(ord('🎈')))
    # print(ord('l'))

def fromVernam(str, k):
    return toVernam(str,k)

def main():
    print("Задание №1 Шифр Цезаря")
    print(toCesar("Hello world!Кодовое слово!АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, абвгдеёжзийклмнопрстуфхцчшщъыьэюя?!", 1))
    print(fromCesar("Hello world!Лпепгпё тмпгп!БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА, бвгдеёжзийклмнопрстуфхцчшщъыьэюяа?!",1))
    print(toCesar("Hello world!Кодовое слово!АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, абвгдеёжзийклмнопрстуфхцчшщъыьэюя?!", 49))
    print(fromCesar("Hello world!Ъюуюсюф быюсю!ПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНО, прстуфхцчшщъыьэюяабвгдеёжзийклмно?!",49))
    print(toCesar('Секретная информация!', 49))
    print()

    print("Задание №2 Шифр Цезаря все варианты")
    fromCesarAll("Hello world!Лпепгпё тмпгп!БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯА, бвгдеёжзийклмнопрстуфхцчшщъыьэюяа?!")
    print()
    fromCesarAll('Бфъафвэпо шэдюаьпёшо!')
    print()

    print("Задание №3 Шифр Вернама")
    res = toVernam('SYSTEM','LONDO')
    print(res)
    print(fromVernam(res,'LONDO'))
    res = toVernam("Hello world!Кодовое слово!АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, абвгдеёжзийклмнопрстуфхцчшщъыьэюя?!", "Задание №3")
    print(res)
    print(fromVernam(res, "Задание №3"))

    res = toVernam('SYSTEM🎈🎇🎆', 'LONDON🎁PaRIS🎞MOSCOW')
    print(res)
    print(fromVernam(res, 'LONDON🎁PaRIS🎞MOSCOW'))


if __name__ == '__main__':
    main()
