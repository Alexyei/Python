import math
import re

pattern = r'\W{0,1}[Ss]?[Hh]e\W'
mainstr = ""
# pattern = re.compile([" she ", " he "])
with open("Hamlet.txt", "r") as inputfile:
    with open("instruction3.txt", "wb") as output:
        bits = []

        for line in inputfile:
            bytes = bytearray()
            words = []
            word = ""
            for c in line:
                if c.isalpha():
                    word += c
                else:
                    if word:
                        words.append(word)
                    word = ""

            j = 0
            while j < len(words):
                word = words[j]
                if word.lower() == "she":
                    bits.append(0)
                elif word.lower() == "he":
                    bits.append(1)
                j += 1

        for i in range(0, len(bits) // 8):
            j = 8 * i
            bytearr = bits[j:j + 8]
            # print(bytearr)
            byte = 0
            # print(bytearr)
            for k in range(0, len(bytearr)):
                byte += int(math.pow(2, k)) * bytearr[-k - 1]
            bytes.append(byte)
        # print(len(bits))
        if len(bits) % 8:
            bits = bits[-(len(bits) % 8):]
        else:
            bits = []
        # print(len(bits))
        mainstr += bytes.decode("ANSI")
        output.write(bytes)
print("zip has created")
print(mainstr)
