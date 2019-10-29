import math

with open("Hamlet.txt", "r") as inputfile:
    with open("instruction2.png", "wb") as output:
        bits = []
        for line in inputfile:
            bytes = bytearray()

            k = 0
            while k < len(line):
                if line[k] == ' ':
                    # print("@"+line)
                    # print(line[k:k+2] == 2)
                    if len(line[k:k+2]) == 2 and line[k+1] == ' ':
                        # print("@"+str(len(line[i:i+2]))+"@", sep="")
                        print(line)
                        bits.append(1)
                        k += 1
                    else:
                        bits.append(0)
                k += 1
            for i in range(0, len(bits) // 8):
                j = 8 * i
                bytearr = bits[j:j + 8]
                # print(bytearr)
                byte = 0
                # print(bytearr)
                for i in range(0, len(bytearr)):
                    byte += int(math.pow(2, i)) * bytearr[-i-1]
                bytes.append(byte)
            # print(len(bits))
            if len(bits) % 8:
                bits = bits[-(len(bits) % 8):]
            else:
                bits = []
            # print(len(bits))
            output.write(bytes)
print("zip has created")
