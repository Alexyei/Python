def four():
    x = 0
    print("in generator start , x =", x)
    while x < 4:
        print("in generator 1, x =", x)
        yield x
        x += 1
        print("in generator 2, x =", x)
    print("in generator end , x =", x)


for i in four():
    print(i)
print()

print(2 in four())
print()
print(-1 in four())
print()
print(0 in four())
print()
print(7 in four())
print()
print([2] in four())
print()
print("*" * 100)


def five():
    x = 0
    print("in generator start , x =", x)
    while x < 4:
        print("in generator 1 , x =", x)
        yield x
        x += 1
        return
        print("in generator 2, x =", x)
    print("in generator end , x =", x)


for i in five():
    print(i)
print()

print(2 in five())
print()
print(-1 in five())
print()
print(0 in five())
print()
print(7 in five())
print()
print([2] in five())
print()
print("*" * 100)


def subgen(x):
    print("in generator start , x =", x)
    for i in range(x):
        print("in generator 1 , x =", x)
        yield i
        print("in generator 2 , x =", x)
    print("in generator end , x =", x)


def gen(y):
    print("in yield from generator start , y =", y)
    yield from subgen(y)
    print("in yield from generator end , y =", y)


for i in gen(3):
    print(i)
print()

print(2 in gen(3))
print()
print(-1 in gen(3))
print()
print(0 in gen(3))
print()
print(7 in gen(3))
print()
print([2] in gen(3))
print()
print("*" * 100)


def genr(y):
    print("in yield from generator start , y =", y)
    yield from subgen(y)
    return [7]
    print("in yield from generator end , y =", y)


for i in genr(3):
    print(i)
print()

print(2 in genr(3))
print()
print(-1 in genr(3))
print()
print(0 in genr(3))
print()
print(7 in genr(3))
print()
print([2] in genr(3))
print()
print(list(gen(3)))
print(list(genr(3)))
print("*" * 100)


def whizbang():
    for i in range(10):
        x = yield i
        print('got sent:', x)


i = whizbang()
print(next(i))
print(next(i))
i.send("hi")
