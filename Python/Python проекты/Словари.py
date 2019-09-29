x = {1: "one", 2: "two"}
x["first"] = "test"
x["first"] = "one"
x[("Delorme", "Ryan", 1995)] = (1, 2, 3)
print(x)
print(x.keys())
print(x.values())
print(list(x.keys()))
print(x[1])
print(x.get(1, "not available"))
print(x.get(4, "not available"))
print()

x = {"one": 7, "two": 4, "three": 3, "four": 17, "five": "abc"}
print(x)
print(x.keys())
print(x.values())
print(x.items())
print()
print(type(x))
print(type(x.keys()))
print(type(x.values()))
print(type(x.items()))
print()

users = {}
for i in range(3):
    name = input(f"name {len(users) + 1}? ")
    age = int(input(f"age {len(users) + 1}? "))
    users[name] = age
print(users)
name = input("search name? ")
print(users.get(name, "not found"))
