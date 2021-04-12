from Stack import Stack
import sys


def main():
    stack = Stack()
    for line in sys.stdin:
        stack.push(line)

    while not stack.isEmpty():
        sys.stdout.write(stack.pop())


if __name__ == '__main__':
    main()
