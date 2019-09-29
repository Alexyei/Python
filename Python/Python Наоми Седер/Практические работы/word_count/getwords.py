from word_count.punct import delpunct


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