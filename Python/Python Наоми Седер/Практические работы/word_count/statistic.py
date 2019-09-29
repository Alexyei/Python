from word_count.getwords import getwordscount


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


def compare_count_of_words(item):
    return item[1]
