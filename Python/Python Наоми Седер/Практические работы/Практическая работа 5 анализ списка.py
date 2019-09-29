def read_data(filename):
    temperatures = []
    with open(filename) as infile:
        for row in infile:
            temperatures.append(float(row.strip()))
    return temperatures


def main():
    temperatures = read_data('lab_05.txt')
    temperatures.sort()
    maxt = max(temperatures)
    mint = min(temperatures)
    averaget = sum(temperatures) / len(temperatures)
    if len(temperatures) % 2 == 0:
        mediant = sum(temperatures[len(temperatures) // 2 - 1:len(temperatures) // 2 + 1]) / 2
    else:
        mediant = temperatures[len(temperatures) // 2]
    uniquet_count = len(set(temperatures))

    print("maxt =", maxt)
    print("mint =", mint)
    print("averaget = %0.2f" % averaget)
    print("mediant = %0.2f" % mediant)
    print("tcount =", len(temperatures))
    print("unique_count =", uniquet_count)


if __name__ == "__main__":
    main()
