import os


def main():
    if not os.path.exists("hello"):
        os.mkdir("hello")
    else:
        print("Указанный файл существует")
    fileExists("users.csv")
    os.rmdir("hello")


def fileExists(filename):
    if os.path.exists(filename):
        print("Указанный файл существует")
    else:
        print("Файл не существует")


if __name__ == "__main__":
    main()
