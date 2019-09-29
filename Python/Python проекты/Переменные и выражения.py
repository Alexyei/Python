import math
import cmath

print('\U0001f604')  # emoji
# x y = 1
# 1X = 1
X1 = 1
x = +2 + 4 * 5 - 6 / 3
print(x)
x = 2 + 4 * (5 - 6) / 3
print(x)
# x = 2+4*[5-6]/3
# print(x)
print([5 - 6])
print(4 * [5 - 6])
print(4 * "text")
# print(4/"text")
# print(4+"text")
# print(4-"text")
# print(4.0*"text")
# print(4.0/"text")
# print(4.0+"text")
# print(4.0-"text")
# help(math)
print(math.cos(math.radians(180)))
print(cmath.sin(18 + 3.1j))
# print(math.cos(math.radians(180+0j)))
print(cmath.sin(18))
print((5 // 2, 5 % 2))
print(divmod(5, 2))
# print(hex(17.1))
# print(oct(17.1))
print(hex(17), hex(-17), oct(17), oct(-17))
number = input("Number? ")
print(number, type(number))
number = float(input("Float? "))
print(number, type(number))
