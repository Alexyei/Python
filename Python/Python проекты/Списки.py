l1 = []
l2 = [1]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 12]
l4 = [1, "two", 3, 4.0, ["a", "b"], (5, 6)]

x = ["first", "second", "third", "fourth"]

print(x)
print(x[0])
print(x[2])
print(x[-1])
print(x[-2])
# print(x[7])
# print(x[-7])
print(x[1:-1])
print(x[0:3])
print(x[-2:-1])
print(x[:3])
print(x[-2:])

x = [1, 2, 3, 4, 5, 6, 7, 8]
print(x)
# (y = x[1:6])[0]=7
y = x[1:6]
y[0] = 7
print(y)
print(x)
x[1] = "two"
print(x[8:9])
print(x[9:8])
print(x[9:10])
x[5:7] = [6.0, 6.5, 7.0]
x[5:7] = (6.0, 6.5, 7.0)
print(x)
print(x[5:])

for i in x[1:]:
    print(i)
print(x)
print(i for i in x)
print([i for i in x])
print(([i for i in x],))
print([i for i in x], )
z = [i for i in x],
print(z)
print(set(i for i in x))
print(set([i for i in x]))
print(set([i for i in x], ))
print()
print(x)
print({6.0, 6.5, 8.0})
x[5:7] = set([6.0, 6.5, 8.0])
print(x)
x[5:7] = []
print(x)
x[5:7] = ()
print(x)
# x[3:5] = None
# [3:5] = 1
# x[-2: -1] = None
x[3:5] = [None]
print(x)
