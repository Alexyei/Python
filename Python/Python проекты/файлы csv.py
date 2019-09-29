import csv


def main():
    FILENAME = "users.csv"

    users = [
        ["Tom", 28],
        ["Alice", 23],
        ["Bob", 34]
    ]

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(users)

    with open(FILENAME, "a", newline="") as file:
        user = ["Sam", 31]
        writer = csv.writer(file, delimiter=';')
        writer.writerow(user)

    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row[0], " - ", row[1], " - ", type(row), type(reader))
    print()

    FILENAME = "dictusers.csv"

    users = [
        {"name": "Tom", "age": 28},
        {"name": "Alice", "age": 23},
        {"name": "Bob", "age": 34}
    ]

    with open(FILENAME, "w", newline="") as file:
        columns = ["name", "age"]
        writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)  # delimiter = ';'
        writer.writeheader()
        writer.writerows(users)
        user = {"name": "Sam", "age": 41}
        writer.writerow(user)

    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=';')  # delimiter = ';'
        for row in reader:
            print(row["name"], " - ", row["age"], " - ", type(row), type(reader))


if __name__ == "__main__":
    main()
