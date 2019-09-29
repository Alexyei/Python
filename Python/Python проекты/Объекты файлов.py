import os

f = open("test_write_file", "w")
# строка завершается пустым символом при записи в файл в текстовом режиме
print(f.write("Первая строка с символом новой строки\n"))
print(f.write("Вторая строка записанная в файл\n"))
f.close()
f = open("test_write_file", "r")

# rstrip удаляет пустые символы в строке спрва и указанные символы в качестве аргумента
line1 = f.readline()
# print(line1+"1")
# №print(1)
print(len(line1))
line2 = f.readline()
print(len(line2))
line1 = line1.rstrip()
print(len(line1))
# print(line1+"1")
# print(1)
line2 = line2.rstrip()
print(len(line2))

f.close()
# в ывод строк через пробел
print(line1, line2)

write_file_dir = os.getcwd()
print(write_file_dir)
# print(os.curdir) point constant
os.chdir(os.path.join("C:\\Users\\Наталия\\Desktop", "Новая папка\\Python\\", "Python проекты"))
print(os.getcwd())
filename = os.path.join("C:\\Users\\Наталия\\Desktop\\", "Новая папка\\Python\\", "Python проекты")
print(filename)
f = open(os.path.join(write_file_dir, "test_write_file"))
print(f.readline())
f.close()

with open(os.path.join(write_file_dir, "test_write_file"), "r") as f:
    for line in f:
        print(line.rstrip())
