def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)


class Fraction:

    def __init__(self, numerator, denominator):
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

    def __str__(self):
        return f'{self._num}/{self._den}'
