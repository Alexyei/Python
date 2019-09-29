def funct1(x, y, z):
    value = x + 2 * y + z ** 2
    if value > 0:
        return x + 2 * y + z ** 2
    else:
        return 0


u, v = 3, 4
print(funct1(u, v, 2))
print(funct1(u, z=v, y=2))
print(funct1(u, 2, z=v))
print()


def funct2(x, y=1, z=1):
    return x + 2 * y + z ** 2


print(funct2(3, z=4))
print()


def funct3(x, y=1, z=1, *tupple):
    print((x, y, z) + tupple)


print(funct3(2))
print(funct3(1, 2, 3, 4, 5, 6, 7, 8, 9))
print()


def funct4(x, y=1, z=1, **kwargs_tupple):
    print(x, y, z, kwargs_tupple)


funct4(1., 2, m=5, n=9, z=3)
print()
