def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDenominatorError

        self._num = numerator
        self._den = denominator
        self._to_lowest_terms()

    def _to_lowest_terms(self):
        num = self._num
        den = self._den

        gcd = _gcd(num, den)

        self._num = num // gcd
        self._den = den // gcd

    def __add__(self, other):
        common_denominator = self._den * other._den
        sum_numerator = other._den * self._num + other._num * self._den
        return Fraction(sum_numerator, common_denominator)

    def __sub__(self, other):
        negative_other = Fraction(-1 * other._num, other._den)
        return self.__add__(negative_other)

    def __eq__(self, other):
        return self._num == other._num and self._den == other._den

    def __repr__(self):
        return f'{self._num}/{self._den}'


class ZeroDenominatorError(ValueError):
    pass
