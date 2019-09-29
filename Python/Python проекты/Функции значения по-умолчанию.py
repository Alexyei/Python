def f1(x=[7, 5]):
    print(x)
    x.append(3)
    print(x)


def f2(x=(7, 5)):
    print(x)
    x += x
    print(x)


def f3(x=[7, 5]):
    print(x)
    x.append(3)
    x = [8]
    print(x)


def main():
    f1()
    f1()
    f1([1])
    f1()
    print()

    f2()
    f2()
    f2((1,))
    f2()
    print()

    f3()
    f3()
    f3([1])
    f3()


if __name__ == "__main__":
    main()
