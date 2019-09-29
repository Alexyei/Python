import re
import math

'str1'
"str2"
'''str3'''
"""str4"""

x = "live and    let \t  \tlive"
print(x.split())
print(x)
print(x.replace("   let \t  \tlive", "enjoy life"))
print(x)

regexpr = re.compile(r"[\t ]+")
print(regexpr.sub(" ", x))
print(x)

e = math.e
x = [1, "two", 3, 4.0, ["a", "b"], (5, 6)]
print("The constant e is:", e, "and the list x is:", x)
print("The value of %s is: %.2f" % ("e", e))

x = "(name, date,\n)"
print(x)
print(x.strip("\n)(,"))
x += "\t"
print(x)
print(x.strip("\n)(,"), len(x))
print(x.strip(), len(x))

y = "frejected"
z = "rejected"
print(y.endswith(z))
print(y.find(z) + len(z) == len(y))
y += "k"
print(y.endswith(z))
print(y.find(z) + len(z) == len(y))
y = "rejected"
print(y.endswith(z))
print(y.find(z) + len(z) == len(y))
y = "ffrejected_kl"
print(y.endswith(z))
print(y.find(z) + len(z) == len(y))
print(y[-len(z):] == z, y[-len(z):], z)
y = "ff_kl_rejected"
print(y.endswith(z))
print(y.find(z) + len(z) == len(y))
print(y[-len(z):] == z, y[-len(z):], z)

z = "Hello, world! Test. Question?"
table = z.maketrans(",.!?", "    ")
print(table, type(table))
print(z.translate(table))

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
print(x)
for i in range(len(x)):
    x[i] = x[i].strip('"')
print(x)

z = "Mississippi"
p_endindex = z.rfind("p")
print(p_endindex, len(z))
z = z[:p_endindex] + z[p_endindex + 1:]
print(z, len(z))

print("{0:10} is the food of gods".format("Ambrosia"))
x = "{1:{0}}".format(3, 4)
print(x)
x = "{0:$>5}".format(3)
print(x)
x = "{0:$<5}".format(3)
print(x)
x = "{a:{b}}".format(a=1, b=5)
print(x)
x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
print(x)
x = "{a:{b}}:{0:$<5}".format(3, 4, a=1, b=5, c=10)
print(x)
