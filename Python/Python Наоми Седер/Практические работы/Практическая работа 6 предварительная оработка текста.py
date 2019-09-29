def main():
    # punct = str.maketrans("", "", "?")
    with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
        for line in infile:
            line = line.lower()
            line = line.replace("--", " ")
            # print(line)
            table = line.maketrans(",.;!?:", " " * 6)
            line = line.translate(table)
            # line = line.strip()
            # punct = str.maketrans("", "", "!.,:;-?")
            # line = line.translate(punct)
            #print(line.encode())
            cleaned_words = line.split()
            # for word in cleaned_words:
            #    outfile.write(word+"\n")
            # print(len(line))
            #if len(line) == 1:
            #    print(line.encode())
            if len(cleaned_words) > 0:  # проверка на пустые строки
                cleaned_words = "\n".join(cleaned_words) + "\n"
                outfile.write(cleaned_words)


if __name__ == "__main__":
    main()
    # print("abc\t d   e\t f\n\r\0e".split())
    # print("\n\t  \t\n\r".split())
    # help(str.maketrans)
