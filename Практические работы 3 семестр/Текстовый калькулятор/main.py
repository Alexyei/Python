import re
from Fraction import Fraction
from calculator import evaluate

# specialPairs = {"одна первая": "1 1 #", "одна вторая": "1 2 #", "одна третья": "1 3 #", "одна четвёртая": "1 4 #",
#                 "одна пятая": "1 5 #",
#                 "одна шестая": "1 6 #", "одна седьмая": "1 7 #", "одна восьмая": "1 8 #", "одна девятая": "1 9 #",
#                 "одна десятая": "1 10 #", "одна одиннадцатая": "1 11 #",
#                 "одна двенадцатая": "1 12 #", "одна тринадцатая": "1 13 #", "одна четырнадцатая": "1 14 #",
#                 "одна пятнадцатая": "1 15 #", "одна шестнадцатая": "1 16 #",
#                 "одна семнадцатая": "1 17 #", "одна восемнадцатая": "1 18 #", "одна девятнадцатая": "1 19 #",
#                 "одна двадцатая": "1 20 #", "одна двадцать первая": "1 20 1 #", "одна двадцать вторая": "1 20 2 #",
#                 "одна двадцать третья": "1 20 3 #", "одна двадцать четвёртая": "1 20 4 #",
#                 "одна двадцать пятая": "1 20 5 #", "одна двадцать шестая": "1 20 6 #",
#                 "одна двадцать седьмая": "1 20 7 #", "одна двадцать восьмая": "1 20 8 #",
#                 "одна двадцать девятая": "1 20 9 #",
#                 "одна тридцатая": "1 30 #", "одна тридцать первая": "1 30 1 #", "одна тридцать вторая": "1 30 2 #",
#                 "одна тридцать третья": "1 30 3 #", "одна тридцать четвёртая": "1 30 4 #",
#                 "одна тридцать пятая": "1 30 5 #", "одна тридцать шестая": "1 30 6 #",
#                 "одна тридцать седьмая": "1 30 7 #", "одна тридцать восьмая": "1 30 8 #",
#                 "одна тридцать девятая": "1 30 9 #",
#                 "одна сороковая": "1 40 #", "одна сорок первая": "1 40 1 #", "одна сорок вторая": "1 40 2 #",
#                 "одна сорок третья": "1 40 3 #", "одна сорок четвёртая": "1 40 4 #",
#                 "одна сорок пятая": "1 40 5 #", "одна сорок шестая": "1 40 6 #",
#                 "одна сорок седьмая": "1 40 7 #", "одна сорок восьмая": "1 40 8 #", "одна сорок девятая": "1 40 9 #",
#                 "одна пятидесятая": "1 50 #", "одна пятьдесят первая": "1 50 1 #", "одна петьдесят вторая": "1 50 2 #",
#                 "одна петьдесят третья": "1 50 3 #", "одна петьдесят четвёртая": "1 50 4 #",
#                 "одна петьдесят пятая": "1 50 5 #", "одна петьдесят шестая": "1 50 6 #",
#                 "одна петьдесят седьмая": "1 50 7 #", "одна петьдесят восьмая": "1 50 8 #",
#                 "одна петьдесят девятая": "1 50 9 #",
#                 "одна шестидесятая": "1 60 #", "одна шестьдесят первая": "1 60 1 #",
#                 "одна шестьдесят вторая": "1 60 2 #",
#                 "одна шестьдесят третья": "1 60 3 #", "одна шестьдесят четвёртая": "1 60 4 #",
#                 "одна шестьдесят пятая": "1 60 5 #", "одна шестьдесят шестая": "1 60 6 #",
#                 "одна шестьдесят седьмая": "1 60 7 #", "одна шестьдесят восьмая": "1 60 8 #",
#                 "одна шестьдесят девятая": "1 60 9 #",
#                 "одна семидесятая": "1 70 #", "одна семьдесят первая": "1 70 1 #",
#                 "одна семьдесят вторая": "1 70 2 #",
#                 "одна семьдесят третья": "1 70 3 #", "одна семьдесят четвёртая": "1 70 4 #",
#                 "одна семьдесят пятая": "1 70 5 #", "одна семьдесят шестая": "1 70 6 #",
#                 "одна семьдесят седьмая": "1 70 7 #", "одна семьдесят восьмая": "1 70 8 #",
#                 "одна семьдесят девятая": "1 70 9 #",
#                 "одна восьмидесятая": "1 80 #", "одна восемьдесят первая": "1 80 1 #",
#                 "одна восемьдесят вторая": "1 80 2 #",
#                 "одна восемьдесят третья": "1 80 3 #", "одна восемьдесят четвёртая": "1 80 4 #",
#                 "одна восемьдесят пятая": "1 80 5 #", "одна восемьдесят шестая": "1 80 6 #",
#                 "одна восемьдесят седьмая": "1 80 7 #", "одна восемьдесят восьмая": "1 80 8 #",
#                 "одна восемьдесят девятая": "1 80 9 #",
#                 "одна девяностая": "1 90 #", "одна девяносто первая": "1 90 1 #",
#                 "одна девяносто вторая": "1 90 2 #",
#                 "одна девяносто третья": "1 90 3 #", "одна девяносто четвёртая": "1 90 4 #",
#                 "одна девяносто пятая": "1 90 5 #", "одна девяносто шестая": "1 90 6 #",
#                 "одна девяносто седьмая": "1 90 7 #", "одна девяносто восьмая": "1 90 8 #",
#                 "одна девяносто девятая": "1 90 9 #",
#                 }

numbers = {"ноль": '0', "один": '1', "одна": '1', "два": '2', "две": '2', "три": '3', "четыре": '4', "пять": '5',
           "шесть": '6', "семь": '7',
           "восемь": '8', "девять": '9', "десять": '10', "одиннадцать": '11', "двенадцать": '12',
           "тринадцать": '13', "четырнадцать": '14', "пятнадцать": '15', "шестнадцать": '16', "семнадцать": '17',
           "восемнадцать": '18', "девятнадцать": '19', "двадцать": '20', "тридцать": '30', "сорок": '40',
           "пятьдесят": '50', "шестьдесят": '60', "семьдесят": '70', "восемьдесят": '80', "девяносто": '90'}
operators = {"плюс": '+', "минус": '-', "умножить на": '*', "разделить на": "/", "и": "?",
             "скобка открывается": "(", "скобка закрывается": ")"}
denominators = {"первых": '1' + ' #', "вторых": '2' + ' #', "третьих": '3' + ' #', "четвёртых": '4' + ' #',
                "пятых": '5' + ' #', "шестых": '6' + ' #',
                "седьмых": '7' + ' #', "восьмых": '8' + ' #', "девятых": '9' + ' #', "десятых": '10' + ' #',
                "одиннадцатых": '11' + ' #',
                "двенадцатых": '12' + ' #', "тринадцатых": '13' + ' #', "четырнадцатых": '14' + ' #',
                "пятнадцатых": '15' + ' #',
                "шестнадцатых": '16' + ' #', "семнадцатых": '17' + ' #', "восемнадцатых": '18' + ' #',
                "девятнадцатых": '19' + ' #',
                "двадцатых": '20' + ' #', "тридцатых": '30' + ' #', "сороковых": '40' + ' #',
                "пятидесятых": '50' + ' #', "шестидесятых": '60' + ' #',
                "семидесятых": '70' + ' #', "восьмидесятых": '80' + ' #', "девяностая": '90' + ' #',
                "первая": '1' + ' #', "вторая": '2' + ' #', "третья": '3' + ' #', "четвёртая": '4' + ' #',
                "пятая": '5' + ' #', "шестая": '6' + ' #',
                "седьмая": '7' + ' #', "восьмая": '8' + ' #', "девятая": '9' + ' #', "десятая": '10' + ' #',
                "одиннадцатая": '11' + ' #',
                "двенадцатая": '12' + ' #', "тринадцатая": '13' + ' #', "четырнадцатая": '14' + ' #',
                "пятнадцатая": '15' + ' #',
                "шестнадцатая": '16' + ' #', "семнадцатая": '17' + ' #', "восемнадцатая": '18' + ' #',
                "девятнадцатая": '19' + ' #',
                "двадцатая": '20' + ' #', "тридцатая": '30' + ' #', "сороковая": '40' + ' #',
                "пятидесятая": '50' + ' #', "шестидесятая": '60' + ' #',
                "семидесятая": '70' + ' #', "восьмидесятая": '80' + ' #', "девяностых": '90' + ' #'
                }


def getKeyByValue(dict, value):
    return list(dict.keys())[list(dict.values()).index(value)]


def wordsToExpression(text):
    text = text.lower()
    # print(re.search(r"[^а-яё ]",text))
    if bool(re.search(r"[^а-яё ]", text)):
        raise SyntaxError("В исходном выражении содержаться недопустимые символы")
    # expression не те символы во входном параметре

    words = dict(numbers)
    words.update(operators)
    words.update(denominators)

    for word, value in words.items():
        # text = text.replace(word,value)
        text = re.sub(fr"\b{word}\b", ' ' + value, text)

    # print(text)
    if bool(re.search(r"[^+\-*/#()?0-9 ]", text)):
        raise SyntaxError("В исходном выражении содержаться недопустимые слова")

    if not balanced(text):
        raise SyntaxError("Скобки раставлены неверно")

    return list(filter(None, text.split(' ')))


def isInt(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def accumulateNumbers(expressionList):
    i = 0
    sumFlag = False
    while (i < len(expressionList)):
        (value, isNumber) = isInt(expressionList[i])
        if isNumber:
            expressionList[i] = value
            if value >= 20 and value % 10 == 0:
                sumFlag = True
            if sumFlag and value < 10:
                # print(expressionList[i - 1:i + 1])
                # print(expressionList[i - 1])
                # print(expressionList[i + 1])
                # print(expressionList[i - 1] + expressionList[i + 1])
                expressionList[i - 1:i + 1] = [expressionList[i - 1] + expressionList[i]]
                i -= 1
                # print(expressionList)
                sumFlag = False
        else:
            sumFlag = False
        i += 1

    return expressionList


def numberExpressionToFractions(numberExpressionList):
    numberExpressionList.append("f")
    # print(numberExpressionList)
    i = 0
    # number = None
    mixedFlag = False
    fraction = []

    def createFraction():
        nonlocal fraction
        nonlocal mixedFlag
        nonlocal i
        if fraction:
            if mixedFlag and len(fraction) == 3:
                frac = Fraction(fraction[0] * fraction[-1] + fraction[1], fraction[-1])
                numberExpressionList[i - 4:i + 1] = [frac]
                i -= 4
                mixedFlag = False
            elif not mixedFlag:
                if numberExpressionList[i] == "#":
                    if len(fraction) == 2:
                        frac = Fraction(fraction[0], fraction[1])
                        numberExpressionList[i - 2:i + 1] = [frac]
                        i -= 2
                    else:
                        raise SyntaxError("Ошибка в записи числа")
                else:
                    if len(fraction) == 1:
                        frac = Fraction(fraction[0], 1)
                        numberExpressionList[i - 1] = frac
                    else:
                        raise SyntaxError("Ошибка в записи числа")
            else:
                raise SyntaxError("Ошибка в записи числа")
            fraction = []

    while (i < len(numberExpressionList)):
        if isinstance(numberExpressionList[i], int):
            # if mixedFlag:
            fraction.append(numberExpressionList[i])
            # elif number is None:
            #     number = numberExpressionList[i]
            # else:
            #     raise SyntaxError("Ошибка в записи числа")
        # elif numberExpressionList[i] in "+-/*()":
        #     fraction = []
        elif numberExpressionList[i] == "?":
            if mixedFlag:
                raise SyntaxError("Дублирование союза 'и' в выражении")
            mixedFlag = True
        else:
            # if fraction:
            #     if mixedFlag and len(fraction) == 3:
            #         frac = Fraction(fraction[0] * fraction[-1] + fraction[1], fraction[-1])
            #         numberExpressionList[i - 4:i + 1] = [frac]
            #         i-=4
            #         mixedFlag = False
            #     elif not mixedFlag:
            #         if numberExpressionList[i] == "#":
            #             if len(fraction) == 2:
            #                 frac = Fraction(fraction[0], fraction[1])
            #                 numberExpressionList[i - 2:i + 1] = [frac]
            #                 i-=2
            #         else:
            #             if len(fraction) == 1:
            #                 frac = Fraction(fraction[0], 1)
            #                 numberExpressionList[i - 1] = frac
            #     else:
            #         raise SyntaxError("Ошибка в записи числа")
            #     fraction = []
            createFraction()
        i += 1

    # i-=1
    # createFraction()
    numberExpressionList.pop()

    return numberExpressionList


def checkFractionExpression(fractionExpression):
    # s - start of list "n()+-*/"
    lastEl = "s"
    canDoublePlusFlag = False
    canDoubleMinusFlag = False
    for i in range(len(fractionExpression)):
        # if not (isinstance(fractionExpression[i],Fraction) and fractionExpression[i] in "+-*/()"):
        #     raise SyntaxError("Ошибка дублирования элементов в выражении")
        # elif
        if isinstance(fractionExpression[i], Fraction):
            if lastEl in "n)":
                raise SyntaxError("Ошибка порядка элементов в выражении")
            lastEl = "n"
        elif fractionExpression[i] in "*/":
            # n)
            if lastEl in "s(*/+-":
                raise SyntaxError("Ошибка порядка элементов в выражении")
            lastEl = fractionExpression[i]
        elif fractionExpression[i] == "+":
            if lastEl in "*/-":
                raise SyntaxError("Ошибка порядка элементов в выражении")
            if lastEl in "n)":
                canDoublePlusFlag = True
            elif lastEl == "+":
                if canDoublePlusFlag:
                    canDoublePlusFlag = False
                else:
                    raise SyntaxError("Недопустимый повтор +")
            lastEl = fractionExpression[i]
        elif fractionExpression[i] == "-":
            if lastEl in "*/+":
                raise SyntaxError("Ошибка порядка элементов в выражении")
            if lastEl in "n)":
                canDoubleMinusFlag = True
            elif lastEl == "-":
                if canDoubleMinusFlag:
                    canDoubleMinusFlag = False
                else:
                    raise SyntaxError("Недопустимый повтор -")
            lastEl = fractionExpression[i]
        elif fractionExpression[i] == "(":
            if lastEl in "n)":
                raise SyntaxError("Ошибка порядка элементов в выражении")
            lastEl = "("
        elif fractionExpression[i] == ")":
            if lastEl in "s*/+-":
                raise SyntaxError("Ошибка порядка элементов в выражении")
            lastEl = ")"
        else:
            raise SyntaxError("Ошибка дублирования элементов в выражении")

    if lastEl in "*/-+(s":
        raise SyntaxError("Выражение не завершенно")


def balanced(s):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        elif c in "}])":
            if stack and c == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def uintToWord(number, words, den=False):
    if number > 20 and number % 10:
        return getKeyByValue(words, str(number - number % 10)) + " " + getKeyByValue(words, str(
            number % 10) + (" #" if den else ""))
    else:
        return getKeyByValue(words, str(number) + (" #" if den else ""))


def fractionToStr(frac):
    result = ""
    # num = frac.getNumerator()
    # den = frac.getDenominator()
    # value = num // den
    #
    # if
    # if value !=0:
    #     num %= den
    #     result = intToWord(value)+" и "
    # result
    (val, num, den) = frac.getElements()
    if any(map(lambda el: abs(el) >= 100, frac.getElements())):
        if den == 1:
            return str(val)
        if val:
            result = str(val) + " и "
        result += str(num) + " / " + str(den)
    else:
        if den == 1:
            if val < 0:
                result = "минус "
                val *= -1
            result += uintToWord(val, numbers)
            return result
        if val:
            if val < 0:
                result = "минус "
                val *= -1

            result += uintToWord(val, numbers) + " и "
        if num < 0:
            result = "минус "
            num *= -1
        result += uintToWord(num, numbers) + " "
        words = dict(numbers)
        words.update(denominators)
        result += uintToWord(den, words, True)

    return result


def evalExpression(expression):
    lstExp = numberExpressionToFractions(accumulateNumbers(wordsToExpression(expression)))
    checkFractionExpression(lstExp)
    result = evaluate(lstExp)
    return fractionToStr(result)


def calculator(expression):
    print(expression)
    try:
        print(" = " + evalExpression(expression))
    except Exception as e:
        print("Ошибка: " + str(e))


def main():
    # test_cases = ("{[()]}", "{[(])}", "{{[[(())]]}}", "()()()((((()))))")
    # for s in test_cases:
    #     print(s, balanced(s))
    # # wordsToExpression("q")
    # print(wordsToExpression("   сорок  два и одиннадцать    двадцать         пятых       "))
    # lst = [1, 2]
    # print(lst[3])
    # print(5 // 3)
    # wordsToExpression("аававдылваыдалвыждыв ваыдлыажа!лвы аывждлаывждлваы аывжлываж")
    # print(accumulateNumbers(wordsToExpression("  сорок   два и одиннадцать    двадцать         пятых       ")))
    # lst = numberExpressionToFractions(accumulateNumbers(wordsToExpression(
    #     "плюс пятьдесят шесть и тридцать семь сорок восьмых минус минус три седьмых разделить на семнадцать умножить на  сорок   два и одиннадцать    двадцать         пятых    плюс  сорок   два и одиннадцать    двадцать         пятых   ")))
    # print(lst)
    # for el in lst:
    #     print(el)
    # print(type(lst[3]))
    # print(accumulateNumbers(wordsToExpression("  плюс пятьдесят шесть и тридцать семь сорок восьмых      ")))
    # checkFractionExpression(lst)
    # # print("s" in "n")
    # lst1 = numberExpressionToFractions(accumulateNumbers(wordsToExpression(
    #     "скобка открывается плюс пять и один вторых плюс скобка открывается минус семь скобка закрывается умножить на девять скобка закрывается разделить на один вторых")))
    # print(lst1)
    # checkFractionExpression(lst1)
    # print(evaluate(lst1))
    # print("u+" in "+-")
    # mydict = {'george': 16, 'amber': 19}
    # print(list(mydict.keys())[list(mydict.values()).index(16)])  # Prints george
    # print(list(mydict.keys()))
    # print(list(mydict.values()).index(16))
    # print(getKeyByValue(mydict,16))
    print("Допустимые выражения: ")
    calculator(evalExpression(
        "скобка открывается плюс пять и одна вторая плюс скобка открывается минус семь скобка закрывается умножить на пять скобка закрывается разделить на одна вторая плюс пять третьих"))
    calculator(
        "скобка открывается плюс пять и одна вторая плюс плюс семь и семь седьмых плюс скобка открывается минус семь скобка закрывается умножить на пять скобка закрывается разделить на одна вторая плюс пять третьих")
    calculator("    пять   плюс     семь   ")
    calculator("скобка открывается скобка открывается пять плюс семь скобка закрывается скобка закрывается")
    calculator("пять умножить на скобка открывается плюс семь скобка закрывается")
    calculator("пять минус минус семь")
    calculator("пять плюс плюс семь")
    calculator("пять плюс скобка открывается минус семь скобка закрывается")
    calculator("минус семь плюс семь и одна четвёртая")
    calculator("девяносто плюс девяносто")
    calculator("девяносто и одна четвёртая плюс девяносто и одна пятая")
    calculator("минус пять девяностых плюс семь пятидесятых")
    longStr = ["скобка открывается скобка открывается" +
               " скобка открывается минус пять плюс пять и одна четвёртая скобка закрывается"+
               " умножить на скобка открывается минус пять и одна восьмая плюс плюс семь и "+
               "две четвёртых скобка закрывается плюс скобка открывается минус ноль умножить на "+
               "скобка открывается плюс семь и одна пятидесятая скобка закрывается разделить на "+
               "скобка открывается минус семь девятых скобка закрывается скобка закрывается скобка закрывается"
               +" плюс скобка открывается плюс семь четвёртых умножить на скобка открывается плюс пять вторых "+
               "скобка закрывается скобка закрывается скобка закрывается разделить на скобка открывается "+
               "пятнадцать и шестнадцать четвёртых умножить на семь вторых скобка закрывается умножить на "+
               "семь и одна четвёртая разделить на скобка открывается минус четыре скобка закрывается "
               +"плюс семь умножить на два и пять вторых"]
    # longStr = ["четыре и тридцать один тридцать вторых разделить на шестьдесят шесть и одна вторая умножить на "+
    #            "скобка открывается минус один и тринадцать шестнадцатых скобка закрывается "
    #            +"плюс семь умножить на два и пять вторых"]
    calculator(*longStr)

    # calculator("скобка открывается минус пять плюс пять и одна четвёртая скобка закрывается умножить на скобка открывается минус пять и одна восьмая плюс плюс семь и две четвёртых скобка закрывается")
    # calculator("ноль умножить на скобка открывается плюс семь и одна пятидесятая скобка закрывается разделить на скобка открывается минус семь девятых скобка закрывается")
    # calculator("минус пятнадцать и шестнадцать четвёртых")
    # calculator("одна четвёртая разделить на скобка открывается минус четыре скобка закрывается")
    # # calculator("девятнадцать тридцать вторых"+" плюс скобка открывается плюс семь четвёртых умножить на скобка открывается плюс пять вторых скобка закрывается скобка закрывается")
    # calculator(" плюс скобка открывается плюс семь четвёртых умножить на скобка открывается плюс пять вторых скобка закрывается скобка закрывается")
    # # calculator("четыре и три восьмых разделить на пятнадцать и шестнадцать четвёртых умножить на семь вторых")
    # calculator("семь и одна четвёртая разделить на скобка открывается минус четыре скобка закрывается")
    # # calculator("четыре и три восьмых разделить на пятнадцать и шестнадцать четвёртых умножить на семь вторых умножить на семь и одна четвёртая разделить на скобка открывается минус четыре скобка закрывается")
    # calculator("пятнадцать и шестнадцать четвёртых умножить на семь вторых")
    # calculator("девятнадцать тридцать вторых плюс четыре и три восьмых")
    # print()
    print("Некорректные выражения")
    calculator("- пять плюс семь")
    calculator("скобка открывается пять плюс семь")
    calculator("скобка открывается скобка открывается пять плюс семь скобка закрывается")
    calculator("скобка закрывается пять плюс семь скобка открывается")
    calculator("пять плюс семь плюс")
    calculator("плюс плюс пять плюс семь")
    calculator("минус минус пять плюс семь")
    calculator("пять умножить семь")
    calculator("пять умножить на плюс семь")
    calculator("пять плюс минус семь")
    calculator("пять скобка открывается плюс скобка закрывается минус семь")
    print()
    while True:
        try:
            print("Введите выражение: ")
            calculator(input())
        except KeyboardInterrupt:
            exit(0)


if __name__ == '__main__':
    main()
    # calculator("восемь девятых умножить на десять и двадцать пятых разделить на шестнадцать восемнадцатых минус семь")
    # a, b = int(input()), int(input())
    # print(list(range(a + a % 2, b + 1, 2)))
    # print(*{'latitude': '37.24N', 'longitude': '-115.81W'})
