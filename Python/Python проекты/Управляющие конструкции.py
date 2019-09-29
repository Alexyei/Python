x = 5
if x < 5:
    y = -1
    z = 5
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10
print(x, y, z)

x = 7
if x < 5:
    y = -1
    z = 5
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10
print(x, y, z)

u, v, x, y = 0, 0, 100, 30
while x > y:
    u += y
    x -= y
    if x < y + 2:
        v += x
        x = 0
    else:
        v += y + 2
        x += -y - 2
print(u, v)

item_list = [3, "string1", 23, 14.0, "string2", 49, 64, 70]
for x in item_list:
    if not isinstance(x, int):
        continue
    if not x % 7:
        print("found an integer divisible by seven: %d" % x)


def swap(a, b):
    a, b = b, a


a = 7
b = 5
print(a, b)
swap(a, b)
print(a, b)

print(type(range), type(range(10)), type(range(10, 12)), type(range(10, 15, 2)))
print(range, range(10), range(10, 12), range(10, 15, 2), list(range(10, 15, 2)), sep="\n")
print()

somelist = [(1, 2), (3, 7), (9, 5)]
result = 0
for t in somelist:
    result += t[0] * t[1]

result = 0
for x, y in somelist:
    result += x * y

x = [1, 3, -7, 4, 9, -5, 4]
for i in range(len(x)):
    if x[i] < 0:
        print("Found a negative number at index ", i)

for i, n in enumerate(x):
    if n < 0:
        print("Found a negative number at index ", i)
print(type(enumerate), type(enumerate(x)))
print(enumerate)
print(enumerate(x))
print(list(enumerate(x)))
print()

x = [1, 2, 3, 4]
y = ['a', 'b', 'c']
z = zip(x, y)
print(type(z))
print(z)
print(list(z))
print()

x = [1, 3, 5, 0, -1, 3, -2]
print(x)
for i, n in enumerate(x):
    if n < 0:
        del x[i]
print(x)
print()

negcount = 0
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
for item in y:
    for n in item:
        if n < 0:
            negcount += 1
print(negcount)
print()


def getstatus(n):
    if n > 5:
        return "very high"
    elif n > 0:
        return "high"
    elif n == 0:
        return "neutral"
    elif n >= -5:
        return "low"
    else:
        return "very low"

x = [5, -5, 7, -8, 1, -2, 0, 7]
