def main():
    wordscount = {}
    with open("moby_01_clean.txt") as infile:
        for line in infile:
            # print(line, type(line), len(line))
            wordscount[line[:-1]] = wordscount.get(line[:-1], 0) + 1

    mincount = min(wordscount.values())
    maxcount = max(wordscount.values())
    print(f"Самые редкие слова встречаются {mincount} раз в тексте")
    for key in wordscount.keys():
        if wordscount[key] == mincount:
            print(key)
    print(f"Самые частые слова встречаются {maxcount} раз в тексте")
    for key in wordscount.keys():
        if wordscount[key] == maxcount:
            print(key)

    # print(wordscount.items())
    # print(wordscount.keys())
    # print(wordscount.values())
    # print(type(wordscount.items()))
    # print(type(wordscount.keys()))
    # print(type(wordscount.values()))
    sorted_words = sorted(wordscount.items(), key=compare_count_of_words)
    # print(sorted_words)
    # print(type(sorted_words))
    print("\nLeast common words:")
    for item in sorted_words[:5]:
        # print(type(item))
        # print(item[0], item[1])
        print(item)
    print("\nMost common words")
    for item in reversed(sorted_words[-5:]):
        # print(type(item))
        # print(item[0], item[1])
        print(item)


def compare_count_of_words(item):
    return item[1]


if __name__ == "__main__":
    main()
