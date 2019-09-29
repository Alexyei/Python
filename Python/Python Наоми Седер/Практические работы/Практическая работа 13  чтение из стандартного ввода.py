import os
from argparse import ArgumentParser


def textstat(filename):
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0
    maxlinelen = -1

    with open(filename) as infile:
        for line in infile:
            line_count += 1
            char_count += len(line)
            byte_count += len(line.encode())
            maxlinelen = max(maxlinelen, len(line))
            words = line.split()
            word_count += len(words)

    return line_count, word_count, char_count, byte_count, maxlinelen


def textstatstdin():
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0
    maxlinelen = -1

    while True:
        try:
            line = input()
            if line == "EOF":  # dont work ctrl+z in PyCharm
                break
            line_count += 1
            char_count += len(line)
            byte_count += len(line.encode())
            maxlinelen = max(maxlinelen, len(line))
            words = line.split()
            word_count += len(words)
        except EOFError:
            break

    return line_count, word_count, char_count, byte_count, maxlinelen


def main():
    parser = ArgumentParser()
    parser.add_argument("input_file", nargs="?", help="read data from this file")
    parser.add_argument("-l", "--lines", dest="lines", help="print lines count", default=False, action="store_true")
    parser.add_argument("-w", "--words", dest="words", help="print words count", default=False, action="store_true")
    parser.add_argument("-m", "--chars", dest="chars", help="print chars count", default=False, action="store_true")
    parser.add_argument("-c", "--bytes", dest="bytes", help="print bytes count", default=False, action="store_true")
    parser.add_argument("-L", "--maxline", dest="maxline", help="print max line length", default=False,
                        action="store_true")

    args = parser.parse_args()
    resultstr = ""
    # print(args)
    if not args.input_file:
        line_count, word_count, char_count, byte_count, maxlinelen = textstatstdin()
    elif os.path.exists(args.input_file):
        line_count, word_count, char_count, byte_count, maxlinelen = textstat(args.input_file)
    else:
        print("File not found")
        return 1

    if not (args.lines or args.words or args.chars or args.bytes):
        resultstr = f"File has {line_count} lines, {word_count} words, {char_count} characters, {byte_count} bytes"
    else:
        if args.lines:
            resultstr = f"File has {line_count} lines"
        if args.words:
            if resultstr:
                resultstr += f", {word_count} words"
            else:
                resultstr = f"File has {word_count} words"
        if args.chars:
            if resultstr:
                resultstr += f", {char_count} characters"
            else:
                resultstr = f"File has {char_count} characters"
        if args.bytes:
            if resultstr:
                resultstr += f", {byte_count} bytes"
            else:
                resultstr = f"File has {byte_count} bytes"

    if args.maxline:
        resultstr += f", max line length {maxlinelen}"

    print(resultstr)


if __name__ == "__main__":
    main()
