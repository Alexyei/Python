def f1():
    x = int(input("number 1? "))
    y = int(input("number 2? "))
    try:
        z = 0
        z = x / y
    except ZeroDivisionError:
        print("Нельзя делить на ноль")
    print(z)
    print()


def f2():
    # Чтобы отключить assert нужно указать в Edit configurations... -> Interpreter options: -O или -OO
    x = int(input("number? "))
    assert x, "number is zero"


def main():
    # f1()
    f2()


if __name__ == "__main__":
    main()
