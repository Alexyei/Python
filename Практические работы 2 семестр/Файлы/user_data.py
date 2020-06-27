import shelve
import os


def create_file(FILENAME):
    fileexists = False
    try:
        with shelve.open(FILENAME, "n") as data_file:
            fileexists = True
        print("Файл создан заново")
    except IOError:
        print("Ошибка при открытии файла")
    choose_next(FILENAME, fileexists)


def delete_file(FILENAME):
    if os.path.isfile(FILENAME + ".dat"):
        os.remove(FILENAME + ".dat")
    if os.path.isfile(FILENAME + ".bak"):
        os.remove(FILENAME + ".bak")
    if os.path.isfile(FILENAME + ".dir"):
        os.remove(FILENAME + ".dir")
    print("Файл удалён")
    choose_next(FILENAME, False)


def append_data(FILENAME):
    try:
        with shelve.open(FILENAME) as data_file:
            print("Удаление данных, для завершения введите stop в качестве названия поля")
            while (True):
                field_name = input("Введите название поля: ")
                if field_name == "stop":
                    break
                field_value = input("Введите значение поля: ")
                try:
                    data_file[field_name] = field_value
                except IOError:
                    print("Ошибка при записи данных в файл")
    except IOError:
        print("Ошибка при открытии файла")
    choose_next(FILENAME, True)


def delete_data(FILENAME):
    try:
        with shelve.open(FILENAME) as data_file:
            print("Ввод или изменение данных, для завершения введите stop в качестве названия поля")
            while (True):
                try:
                    if not data_file:
                        print("Файл пуст")
                        break
                    field_name = input("Введите название поля: ")
                    if field_name == "stop":
                        break

                    if field_name in data_file:
                        del data_file[field_name]
                        print("Поле " + field_name + " удалено")
                    else:
                        print("Поле " + field_name + " отсутствует в файле")
                except IOError:
                    print("Ошибка при удалении данных в файл")
    except IOError:
        print("Ошибка при открытии файла")
    choose_next(FILENAME, True)


def read_file(FILENAME):
    try:
        with shelve.open(FILENAME) as data_file:
            try:
                if not data_file:
                    print("Файл пуст")
                for field in data_file.items():
                    print(field[0] + " : " + field[1])
            except IOError:
                print("Ошибка при чтении данных из файла")
    except IOError:
        print("Ошибка при открытии файла")
    choose_next(FILENAME, True)


def input_comand(can_use):
    while (True):
        action = input()
        if action in can_use:
            return action
        else:
            print("Введено недопустимое значение. Повторите ввод")


def choose_next(FILENAME, fileexist):
    actions = {
        "1": create_file,
        "2": delete_file,
        "3": append_data,
        "4": delete_data,
        "5": read_file,
        "6": get_filename,
        "7": exit_programm
    }

    print("Выберите следующие действие:")
    if fileexist:
        print(
            "1 - очистить файл, 2 - удалить файл, 3 - добавить или изменить данные, 4 - удалить данные, 5 - прочитать данные, 6 - указать новый путь к файлу, 7 - выйти из программы")
        actions[input_comand(list(actions.keys()))](FILENAME)
    else:
        print("1 - создать файл, 6 - указать новый путь к файлу, 7 - выйти из программы")
        actions[input_comand(["1", "6", "7"])](FILENAME)


def get_filename(*args):
    FILENAME = input("Введите путь к файлу (без расширения):\n")
    fileexist = False
    if os.path.isfile(FILENAME + ".dat"):
        print("Файл найден")
        fileexist = True
    else:
        print("Файл не найден")
    choose_next(FILENAME, fileexist)


def exit_programm(*args):
    exit(0)


def main():
    get_filename()


if __name__ == "__main__":
    main()
