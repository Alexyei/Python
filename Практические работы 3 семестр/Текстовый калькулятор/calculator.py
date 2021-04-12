from Fraction import Fraction


def is_op(el):
    return el in "+-*/"


def priority(op):
    if "u" in op:
        return 3
    if op in "+-":
        return 1
    elif op in "*/":
        return 2
    return -1


def process_op(stack, op):
    if "u" in op:
        l = stack.pop()
        {
            "u+": lambda: stack.append(l),
            "u-": lambda: stack.append(Fraction(-l.getNumerator(),l.getDenominator())),
        }[op]()
    else:
        r = stack.pop()
        l = stack.pop()
        {
            '+': lambda: stack.append(l + r),
            '-': lambda: stack.append(l - r),
            '*': lambda: stack.append(l * r),
            '/': lambda: stack.append(l / r)
        }[op]()


def evaluate(expressionList):
    numbers = []
    operators = []
    may_be_unary = True
    for i in range(len(expressionList)):
        if isinstance(expressionList[i], Fraction):
            numbers.append(expressionList[i])
            may_be_unary = False
        elif expressionList[i] == '(':
            operators.append('(')
            may_be_unary = True
        elif expressionList[i] == ')':
            while (operators[-1] != '('):
                process_op(numbers, operators.pop())
            # elif is_op(expressionList[i]):
            operators.pop()
            may_be_unary = False
        else:
            if may_be_unary and expressionList[i] in "+-":
                expressionList[i] = "u" + expressionList[i]
            # while(operators and priority(operators[-1]) >= priority(expressionList[i])):
            while (operators and (
                    (len(expressionList[i]) == 1 and priority(operators[-1]) >= priority(expressionList[i])) or
                   (len(expressionList[i]) == 2 and priority(operators[-1]) > priority(expressionList[i])))):
                if (len(expressionList[i]) == 2 and priority(operators[-1]) > priority(expressionList[i])):
                    print("OMG!!!!!")
                process_op(numbers, operators.pop())
            operators.append(expressionList[i])
            may_be_unary = True
            # else:
            #     numbers.append(expressionList[i])

    while (operators):
        process_op(numbers, operators.pop())

    return numbers[-1]
# lst = [1,2,3,7,8]
#
# def test(lst):
#     lst.pop()
#     lst.append(7)
#
# test(lst)
#
# print(lst)
