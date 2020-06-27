import math


# задание 1
# Задание1: реализовать программу, рекомендующую стиль одежды с учетом 4
# режимов температуры и 4 видов осадков
# программа должна выдавать рекомендации на все возможные комбинации
def weather1():
    temp = int(input('Введите значение температуры: '))  # вводим значение температуры
    weather = int(input(
        'Какая на улице погода?(Введите 1 если есть дождь и 2 - если снег, 3 - если град или 0 если осадков нет)\n'))

    if temp > 20:
        print('одевайтесь легко, т.к. на улице жарко', end='')
    elif 20 >= temp > 1:
        print('не забудьте верхнюю обежду, на улице прохдадно', end='')
    elif 0 >= temp >= -15:
        print('одевайтесь тепло, на улице холодно', end='')
    else:
        print('сидите дома, на улице слишком холодно')
        return

    if weather == 1:  # дождь
        print(' и возьмите зонт')
    elif weather == 2:  # снег
        print(' и возможно следует одеть шапку')
    elif weather == 3:  # град
        print(', но подождите пока закончится град')
    else:  # без осадков
        print()


# задание 3
# доработать программный код на все возможные комбинации температуры и осадков
def weather3():
    print('что одеть?')
    temp = int(input("введите значение температуры "))
    pogoda = input("дождь, снег, ветер, ясно ")

    if temp > 20:
        if pogoda == 'дождь':
            print('можете одеть шорты с футболкой, но возьмите зонт')
        elif pogoda == 'снег':
            print('что то не то с погодой, возможно конец близок')
        elif pogoda == 'ветер':
            print('оденьте ветровку')
        else:
            print('одеваитесь легко на улице жарко')
    elif 20 >= temp > 1:
        if pogoda == 'дождь':
            print('одеваитесь теплее и возмите зонт')
        elif pogoda == 'снег':
            print('возможно зима уже близко')
        elif pogoda == 'ветер':
            print('оденьте шапку')
        else:
            print('одевайте осеннюю одежду')
    elif 0 >= temp >= -15:
        if pogoda == 'дождь':
            print('возможно весна уже близко')
        elif pogoda == 'снег':
            print('одеваите зимние вещи и бегом на улицу, погода класс!!!')
        elif pogoda == 'ветер':
            print('одевайтесь теплее')
        else:
            print('погода класс!!!')
    else:
        if pogoda == 'дождь':
            print('аномальная погода')
        elif pogoda == 'снег':
            print('настоящая зима')
        elif pogoda == 'ветер':
            print('сидите дома, на улице слишком холодно')
        else:
            print('Мороз и солнце; день чудесный!')


# задание 4
# реализовать программу для нахождения квадратного уравнения через Дискриминант
# учесть частный случай, когда Дискриминант = 0 и корень уравнения один
def solveSqrEqual(a=0, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + math.sqrt(d)) / 2 * a, (-b - math.sqrt(d)) / 2 * a
    if d == 0:
        return -b / 2 * a


# задания 5-6
# первая функция
def function1():
    f_range = (2.0, 3.0)
    f_step = 0.1
    x = f_range[0]
    # (math.cos(math.radians(x)) ** 2) / (1 + math.sin(math.radians(x)))
    f_expression = lambda x: (math.cos(math.radians(x)) ** 2) / (1 + math.sin(math.radians(x))) - math.log(
        x / math.pow(x - 1, 1 / 3)) ** 2
    for i in range(0, int((f_range[1] - f_range[0]) / f_step) + 1):
        try:
            print("x = {0:.4f}; y = {1:.4f}".format(x, f_expression(x)))
        except ValueError:
            print("x = {0:.4f}; вне области допустимых значений функции".format(x))
        x += f_step


# задания 5-6
# вторая функция
def function2():
    N = int(input('Введите N: '))
    if N < 1:
        raise ValueError("Число не являеться натуральным")
    M = S = 1
    while (S <= N):
        M += 1
        S += M ** 2
    return M - 1


# задания 5-6
# третья функция
def function3():
    a = float(input('Введите a: '))
    if a < 0:
        raise ValueError("a должна быть положительным числом")
    c = float(input('Введите c: '))
    if c < 0:
        raise ValueError("c должна быть положительным числом")
    R = float(input('Введите R: '))
    if R < 0:
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
    weather1()
    weather1()

    print("Задание №3")
    weather3()
    weather3()

    print("Задание №4")
    x = solveSqrEqual(1, 3, -4)
    print(f"Решние уравнения x^2 +3x -4 = 0: x1 = {x[0]}, x2 = {x[1]}")
    print(f"Решние уравнения x^2 -4x -4 = 0: x = {solveSqrEqual(1, -4, 4)}")
    print(f"Решние уравнения x^2 -5x +9 = 0: x = {solveSqrEqual(1, -5, 9)}")
    print()

    print("Задания №5-6")
    print("Первая функция")
    function1()
    print()

    print("Вторая функция")
    print(f"M = {function2()}")
    print()

    print("Третья функция")
    print("y = {0:.4f}".format(function3()))


if __name__ == "__main__":
    main()
