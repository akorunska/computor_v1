from .get_formalized_equation import count_digits_after_decimal_point
from .custom_math import *


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a + other.a, self.b + other.b)
        return ComplexNumber(self.a + other, self.b)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.a - other.a, self.b - other.b)
        return ComplexNumber(self.a - other, self.b)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.a * other, self.b * other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return ComplexNumber(self.a / other, self.b / other)

    def __str__(self):
        a_digits = count_digits_after_decimal_point(self.a)
        b_digits = count_digits_after_decimal_point(self.b)
        sign = '+' if self.b > 0 else '-'
        return "%.*f %s %.*f * i" % (a_digits, self.a, sign, b_digits, abs(self.b))

    @staticmethod
    def sqrt(value):
        srt_of_module = sqrt(abs(value))
        if value >= 0:
            return srt_of_module
        return ComplexNumber(0, -1 * srt_of_module), ComplexNumber(0, srt_of_module)

