def main():
    print("Задание №1")
    PC_energy = [("видекарта", 75), ("процессор", 58), ("материнская плата", 30), ("DDR4 - 8Гб", 20),
                 ("DDR4 - 8Гб", 20), ("SSD - 1Тб", 10), ("монитор", 15)]
    print(PC_energy)
    print()

    print("Задания №№2-4")
    print(f"Колличество элементов компьютера: {len(PC_energy)}")
    print(f"Монитор входит в борку? {'монитор' in [item[0] for item in PC_energy]}")
    print(f"SSD входит в борку? {any(['SSD' in item[0] for item in PC_energy])}")
    print()

    print("Задание №5")
    print("Элементы компьютера: ")
    for item in PC_energy:
        print(item[0])
    print()

    print("Задание №6")
    print(f"Элемент с наибольшим электропотреблением: {max(PC_energy, key=lambda item: item[1])[0]}")
    print(f"Элемент с наименьшим электропотреблением: {min(PC_energy, key=lambda item: item[1])[0]}")
    print(f"Общее энергопотребление компонентов компьютера: {sum([item[1] for item in PC_energy])}")
    print()

    print("Задание №7")
    input_item = input("Введите название элемента: ")
    print(f"Колличество данных элементов в компьютере: {[input_item in item[0] for item in PC_energy].count(True)}")
    print()

    print("Задание №8")
    dict_PC = {}
    for item in PC_energy:
        if item[0] in dict_PC:
            dict_PC[item[0]] += item[1]
        else:
            dict_PC[item[0]] = item[1]
    print(dict_PC.items())
    print()

    print("Задание №9")
    PC_energy.sort(reverse=True, key=lambda item: item[1])
    print("Элементы компьютера: ")
    for item in PC_energy:
        print(f"{item[0]}: {item[1]}")
    print()


if __name__ == "__main__":
    main()
