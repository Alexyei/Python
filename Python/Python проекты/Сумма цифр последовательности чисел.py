import sys

n = int(sys.stdin.readline())
sumdigits = 0
for i in range(1, n + 1):
    # print([int(digit) for digit in list(str(i))])
    sumdigits += sum([int(digit) for digit in list(str(i))])
sys.stdout.write(str(sumdigits))
