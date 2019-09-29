def getwordscount(filename):
    wordscount = {}
    try:
        with open(filename) as infile:
            try:
                for line in infile:
                    # print(line, type(line), len(line))
                    wordscount[line[:-1]] = wordscount.get(line[:-1], 0) + 1
            except IOError:
                print("Ошибка при чтении из файла")
    except IOError:
        print("Ошибка при открытии файла")
    return wordscount


def printkeys(dictionary, value):
    for key in dictionary.keys():
        if dictionary[key] == value:
            print(key)


def printcollection(collection):
    for item in collection:
        print(item)


def wordsstatistic(filename):
    wordscount = getwordscount(filename)
    if not wordscount:
        print("Получен пустой словарь слов")
        return
    mincount = min(wordscount.values())
    maxcount = max(wordscount.values())
    print(f"Самые редкие слова встречаются {mincount} раз в тексте")
    printkeys(wordscount, mincount)
    print(f"Самые частые слова встречаются {maxcount} раз в тексте")
    printkeys(wordscount, maxcount)

    sorted_words = sorted(wordscount.items(), key=compare_count_of_words)
    print("\nLeast common words:")
    printcollection(sorted_words[:5])

    print("\nMost common words")
    printcollection(reversed(sorted_words[-5:]))


def delpunct(line):
    line = line.lower()
    line = line.replace("--", " ")
    table = line.maketrans(",.;!?:", " " * 6)
    line = line.translate(table)
    return line


def words(line):
    cleaned_words = line.split()
    if len(cleaned_words) > 0:  # проверка на пустые строки
        cleaned_words = "\n".join(cleaned_words) + "\n"
        return cleaned_words


def texttowords(textfilename, outfilename):
    try:
        with open(textfilename) as infile, open(outfilename, "w") as outfile:
            try:
                for line in infile:
                    cleaned_words = words(delpunct(line))
                    if cleaned_words:
                        outfile.write(cleaned_words)
            except IOError:
                print("Ошибка при чтении из файла")
    except IOError:
        print("Ошибка при открытии файла")


def main():
    texttowords("moby_01.txt", "moby_01_clean.txt")
    wordsstatistic("moby_01_clean.txt")
    # mincount = min({}.values())
    # maxcount = max({}.values())
    # print(mincount, maxcount)


def compare_count_of_words(item):
    return item[1]


if __name__ == "__main__":
    main()
