def decorate(func):
    print("in decorate function, decorating", func.__name__)

    def wrapper_func(*args):
        print("Executing", func.__name__)
        return func(*args)

    return wrapper_func


def myfunction(parametr):
    print(parametr)
    return [7]


myfunction = decorate(myfunction)
print("*" * 100)
print(myfunction("hello"))
print("*" * 100)
print()


@decorate
def myfunction_d(parametr):
    print(parametr)
    return [8]


print("*" * 100)

print(myfunction_d("hello"))
print("*" * 100)
print()


@decorate
def myfunction_e(parametr):
    print(parametr)


print("*" * 100)

print(myfunction_e("hello"))
print("*" * 100)
print("*" * 100)
print()

mydecorate = decorate

myfunction = mydecorate(myfunction)
print("*" * 100)
print(myfunction("hello"))
print("*" * 100)
print()


@mydecorate
def myfunction_d(parametr):
    print(parametr)
    return [8]


print("*" * 100)

print(myfunction_d("hello"))
print("*" * 100)
print()


@mydecorate
def myfunction_e(parametr):
    print(parametr)


print("*" * 100)

print(myfunction_e("hello"))
print("*" * 100)
print()


def decorate(func):
    def wrapper_func(*args):
        return f"<html>{func(*args)}</html"

    return wrapper_func


@decorate
def myfunction(parametr):
    return parametr


print(myfunction("hello"))
