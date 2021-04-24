import sys

def main():
    stack = []
    for line in sys.stdin:
        stack.append(line)

    for line in range(len(stack)-1,-1,-1):
        sys.stdout.write(stack[line])


if __name__ == '__main__':
    main()