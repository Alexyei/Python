# from word_count import *
from word_count.statistic import wordsstatistic
from word_count.getwords import texttowords


def main():
    # getwords.texttowords("moby_01.txt", "moby_01_clean.txt")
    # statistic.wordsstatistic("moby_01_clean.txt")

    texttowords("moby_01.txt", "moby_01_clean.txt")
    wordsstatistic("moby_01_clean.txt")


if __name__ == "__main__":
    main()
