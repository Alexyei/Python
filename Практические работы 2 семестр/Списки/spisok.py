# Задание №1
# Нaпишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его cоседей.
# Для элeментов списка, являющиxся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка.
# Например, если на вход подаётся cписок «1 3 5 6 10»,
# то на выход ожидается cписок «13 6 9 15 7».
# Если на вход пришло только однo число, надо вывести его же.
# Вывoд должен содержать одну строку с чиcлами новoго списка, разделёнными пробeлом.
def sumNeighbors(strlist):
    numbers = [int(num) for num in strlist.split(' ')]
    if len(numbers) == 1:
        return str(numbers[0])
    return ' '.join([str(numbers[i - 1] + numbers[(i + 1) % len(numbers)]) for i in range(len(numbers))])


# Задание №2
def repeatElements(strlist):
    numbers = [int(num) for num in strlist.split(' ')]
    return ' '.join(set([str(i) for i in numbers if numbers.count(i) > 1]))


# Задание №3
def colsWithNumber(matrix, number):
    cols = []
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == number:
                cols.append(j)
                break
    return cols


# Задание №4
def listSimmetric(strlist):
    numbers = [int(num) for num in strlist.split(' ')]
    return all([numbers[i] == numbers[-(i + 1)] for i in range(int(len(numbers) / 2))])


# Задание №5
def listCheckOrder(data, countdel=2):
    if len(data) < countdel + 2:
        return True
    count = 0
    j = 0
    datalist = data[:]
    while j < len(datalist) - 1:
        for i in range(len(datalist) - 1):
            if datalist[i] > datalist[i + 1]:
                # print(datalist[i+1])
                count += 1
                del datalist[i + 1]
                # print(datalist)
                break
        j += 1

    if count <= countdel:
        return True

    count = 0
    j = 0
    datalist = data[:]
    while j < len(datalist) - 1:
        for i in range(len(datalist) - 1):
            if datalist[i] < datalist[i + 1]:
                count += 1
                del datalist[i + 1]
                break
        j += 1
    return count <= countdel


# Задание №6
def countUniqueElements(strlist):
    return len(set([num for num in strlist.split(' ')]))


# Задание №7
def uniqueElements(strlist):
    numbers = [num for num in strlist.split(' ')]
    i = 0
    while (i < len(numbers) - 1):
        j = i + 1
        while (j < len(numbers)):
            if numbers[i] == numbers[j]:
                del numbers[j]
            else:
                j += 1
        i += 1

    return ' '.join(numbers)


def equalSetLists(list1, list2):
    return set(list1) == set(list2)


def function2():
    while (True):
        N = int(input('Введите N: '))
        try:
            if N < 1:
                raise Exception("Число не являеться натуральным")
        except Exception as e:
            print(e)
            print("Повторите ввод")
            continue
        break
    M = S = 1
    while (S <= N):
        M += 1
        S += M ** 2
    return M - 1


def getCPUbyModel(CPUs, model):
    for (key, value) in CPUs.items():
        if key[1] == model:
            return key, value
    return None


def function3():
    a = float(input('Введите a: '))
    if a <= 0:
        raise ValueError("a должна быть положительным числом")
    c = float(input('Введите c: '))
    if c <= 0:
        raise ValueError("c должна быть положительным числом")
    R = float(input('Введите R: '))
    if R <= 0:
        raise ValueError("Радиус должен быть положительным числом")
    x = float(input('Введите x: '))
    if x < -R:
        return 0
    elif x < 0:
        return math.sqrt(R ** 2 - x ** 2)
    else:
        return x * a / c


def main():
    print("Задание №1")
    print(sumNeighbors("7"))
    print(sumNeighbors("7 8"))
    print(sumNeighbors("1 3 5 6 10"))
    print()

    print("Задание №2")
    print(repeatElements("7"))
    print(repeatElements("-4 8"))
    print(repeatElements("-4 -4 8 7 9 2 -7 7 -11 -4 7 -7"))
    print(repeatElements("4 8 0 3 4 2 0 3"))
    print()

    print("Задание №3")
    print(colsWithNumber([[0, 0, -1, 9, 0],
                          [0, 7, 0, 12, -4],
                          [17, 10, 0, 17, 10],
                          [12, -5, 0, 0, 7],
                          [7, -11, 0, 77, 0]], 7))
    print(colsWithNumber([[]], -7))
    print(colsWithNumber([[0, 0, -1, 9, 0, 12],
                          [0, 7, 0, 12, -4, -4],
                          [17, 10, 0, 17, 10, 0],
                          [12, -5, 0, 0, 7, 9],
                          [7, -11, 0, 77, 0, 11]], -4))
    print(colsWithNumber([[0, 0, -1, 9, 0],
                          [0, 7, 0, 12, -4],
                          [17, 10, 0, 17, 10]], 17))
    print(colsWithNumber([[0, 0, -1, 9, 0],
                          [0, 7, 0, 12, -4],
                          [17, 10, 0, 17, 10]], 8))
    print()

    print("Задание №4")
    print(listSimmetric(input("Введите последовательность чисел через пробел: ")))
    print(listSimmetric("1 -2 3 -2 7"))
    print(listSimmetric("1"))
    print(listSimmetric("1 -2 3 -2"))
    print(listSimmetric("1 -2 -2 1"))
    print()

    print("Задание №5")
    print(listCheckOrder(list(map(lambda x: int(x), input("Введите последовательность чисел через пробел: ").split()))))
    print(listCheckOrder([1, 2, 3]))
    print(listCheckOrder([-1, -2, -3]))
    print(listCheckOrder([-1, -2, -3, -3]))
    print(listCheckOrder([-1, -2, -3, -4, 1, 2, 3]))
    print(listCheckOrder([1, 2, 3, 4, -1, -2, -3]))
    print(listCheckOrder([2, 3, 4, 1, 3, 5]))
    print(listCheckOrder([-2, -3, -4, -1, -3, -5]))
    print()

    print("Задание №6")
    print(countUniqueElements(input("Введите последовательность чисел через пробел: ")))
    print(countUniqueElements("1 -2 3"))
    print(countUniqueElements("1 -2 7 3 -2 1 7 7"))
    print()

    print("Задание №7")
    print(uniqueElements(input("Введите последовательность чисел через пробел: ")))
    print(uniqueElements("1 -2 3"))
    print(uniqueElements("1 -2 7 3 -2 1 7 7"))
    print()

    print("Задание №8")
    books = list(
        map(lambda s: s.strip(), input("Введите упорядоченный по алфавиту список книг через запятую:\n").split(',')))
    book = input("Введите ещё одну книгу: ")
    books.append(book)
    books.sort()
    print("Упорядоченный по алфавиту список книг: ")
    for book in books:
        print(book)
    print()

    print("Задание №9")
    numbers = [-1, 0, 7, 18, 15, -4, 7, 11, 0, -100, 100, 20, 17, -18, 17, 16, 24, 27]
    # print(len(numbers))
    # print(list(range(0, len(numbers) - 1, 2)))
    # print(list(range(0, len(numbers), 2)))
    numbers1 = numbers[:]
    print("Исходный список: ")
    print(numbers)
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > 0 and numbers[j] > 0 and numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print("Сортировка положительных значений: ")
    print(numbers)
    numbers = numbers1
    for i in range(0, len(numbers) - 1, 2):
        for j in range(i + 2, len(numbers), 2):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print("Сортировка чётных элементов: ")
    print(numbers)
    print()

    print("Задание №10")
    print(equalSetLists(numbers, numbers[:]))
    print(equalSetLists([1, 2, 3, 4, -4, 4], [1, 2, 3, 4, -4, 4, 4, 1]))
    print(equalSetLists([1, 2, 3, 4, -4, 4], [1, 2, 3, 4, -4, 4, 4, -1]))
    print()

    print("Обработка исключений")
    print("Exception")
    print(function2())
    print()

    print("AttributeError")
    try:
        x = ++function2.result
    except AttributeError:
        print("У функции нет свойства result")
    print()

    print("IndexError")
    try:
        print(getCPUbyModel({"a": 1}, "Ryzen 5 1700"))
    except IndexError:
        print("Неправильный формат данных")
    print()

    print("KeyError")
    processors = {("Ice Lake", "1068G7"): (4, 8), ("Ice Lake", "1005G1"): (2, 4), ("Zen", "Ryzen 5 1600X"): (6, 12),
                  ("Zen", "Ryzen 7 1700"): (8, 16), ("Kaby Lake", "7640X"): (4, 4)}
    try:
        print(processors["Ryzen 5 1700"])
    except KeyError:
        print("Неправильный поиск по словарю")
    print()

    print("ValueError")
    while (True):
        try:
            print(function3())
        except ValueError as e:
            print(e)
            print("Повторите ввод параметров")
            continue
        break
    print()


if __name__ == "__main__":
    main()
