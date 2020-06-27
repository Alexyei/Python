import csv


def countStudents(students):
    try:
        if not students:
            raise Exception("Список студентов пуст")
        if type(students) != list:
            raise Exception("Список студентов не является списком")

        result = [0, 0, 0, 0]
        for student in students:
            if student[1] not in range(1, 5):
                raise Exception("Недопустимое значение класса студента")
            result[student[1] - 1] = result[student[1] - 1] + 1

    except Exception as e:
        print("Ошибка при обработке списка студентов:")
        print(e)
        return (0, 0, 0, 0)
    return tuple(result)


def writeinCSV(FILENAME, result):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            try:
                writer.writerow(result)
            except IOError:
                print("Ошибка при записи данных в файл")
        print("Файл создан")
    except IOError:
        print("Ошибка при создании файла")


def readfromCSV(FILENAME, result):
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file, delimiter=';')
            try:
                for row in reader:
                    return tuple([int(value) for value in row[0:4]])
            except IOError:
                print("Ошибка при чтении данных из файла")
    except IOError:
        print("Ошибка при открытии файла")


def main():
    FILENAME = "ЗБ-ПИ1-1 Белоусов 5 вариант контрольная students.csv"
    students = [('Иванов', 2), ('Петров', 3), ('Сидоров', 2)]
    result = countStudents(students)
    print(result)
    writeinCSV(FILENAME, result)
    print(readfromCSV(FILENAME, result))
    print()

    students = students + [('Голубикин', 1), ('Синицин', 4), ('Патапов', 4), ('Крамеров', 1), ('Гавриков', 3),
                           ('Лимонов', 1), ('Новиков', 3), ('Тарасов', 1)]
    result = countStudents(students)
    print(result)
    writeinCSV(FILENAME, result)
    print(readfromCSV(FILENAME, result))
    print()
    print(countStudents([]))
    print(countStudents((5, 7)))
    students[7] = ('Полкин', 5)
    print(countStudents(students))


if __name__ == "__main__":
    main()
