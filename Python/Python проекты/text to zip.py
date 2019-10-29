import math

with open("Hamlet.txt", "r") as inputfile:
    with open("text.zip", "wb") as output:
        bits = []
        for line in inputfile:
            bytes = bytearray()

            for char in line:
                if char == ',':

                    bits.append(0)
                    # print(bits)
                elif char == ';':
                    bits.append(1)
                    # print(bits)
            for i in range(0, len(bits) // 8):
                j = 8 * i
                bytearr = bits[j:j + 8]
                # print(bytearr)
                byte = 0
                # print(bytearr)
                for i in range(0, len(bytearr)):
                    byte += int(math.pow(2, i)) * bytearr[-i-1]
                bytes.append(byte)
            print(len(bits))
            if len(bits) % 8:
                bits = bits[-(len(bits) % 8):]
            else:
                bits = []
            print(len(bits))
            output.write(bytes)
print("zip has created")
