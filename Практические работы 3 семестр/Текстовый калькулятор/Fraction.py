class Fraction:
    def _reduce(self, numerator, denominator):
        if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
            sign = -1
        else:
            sign = 1

        a = abs(numerator)
        b = abs(denominator)

        i = min(a, b)
        if (i == 0):
            return

        while ((a % i != 0) or (b % i != 0)):
            i -= 1

        a //= i
        b //= i

        return (a * sign, b)

    def getNumerator(self):
        return self._numerator

    def getDenominator(self):
        return self._denominator

    def getElements(self):
        if (self._numerator < 0 and self._denominator >= 0) or (self._numerator >= 0 and self._denominator < 0):
            sign = -1
        else:
            sign = 1

        num = abs(self._numerator)
        den = abs(self._denominator)
        val = num // den
        if val:
            num%=den
            val*=sign
        else:
            num*=sign

        return (val, num, den)


    def __init__(self, numerator, denominator):
        if (not isinstance(numerator, int)):
            raise TypeError("The numerator of a Faction must be an integer")
        if (not isinstance(denominator, int)):
            raise TypeError("The denominator of a Faction must be an integer")

        if (denominator == 0):
            raise ZeroDivisionError("Знаменатель дроби не может быть нулём")

        if (numerator == 0):
            self._numerator = 0
            self._denominator = 1
        else:
            # if (numerator<0 and denominator>=0) or (numerator>0 and denominator<0):
            #     sign = -1
            # else:
            #     sign = 1
            (self._numerator, self._denominator) = self._reduce(numerator, denominator)

    def __str__(self):
        return str(self._numerator) + "/" + str(self._denominator)

    def __eq__(self, other):
        return (self.getNumerator() == other.getNumerator()) and (self.getDenominator() == other.getDenominator())

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.getNumerator() * other.getDenominator() < self.getDenominator() * other.getNumerator()

    def __le__(self, other):
        return not other < self

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not other > self

    def __add__(self, other):
        num = self.getNumerator() * other.getDenominator() + other.getNumerator() * self.getDenominator()
        den = self.getDenominator() * other.getDenominator()
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.getNumerator() * other.getDenominator() - other.getNumerator() * self.getDenominator()
        den = self.getDenominator() * other.getDenominator()
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.getNumerator() * other.getNumerator()
        den = self.getDenominator() * other.getDenominator()
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.getNumerator() * other.getDenominator()
        den = self.getDenominator() * other.getNumerator()
        return Fraction(num, den)
