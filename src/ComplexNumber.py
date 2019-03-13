from .get_formalized_equation import count_digits_after_decimal_point


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
        eps = 0.00000001
        current_value = abs(value)
        prev_value = 0
        while abs(prev_value - current_value) > eps:
            prev_value = current_value
            current_value = 1 / 2 * (current_value + abs(value)/current_value)
        if value >= 0:
            return current_value
        return ComplexNumber(0, -1 * current_value), ComplexNumber(0, current_value)

