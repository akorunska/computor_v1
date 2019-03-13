
def count_digits_after_decimal_point(val: float):
    s = str(val)
    if '.' not in s:
        return 0
    if s[-2:] == '.0':
        return 0
    return len(s) - s.index('.') - 1


def get_formalized_equation(coef: list):
    result = ""
    for c, i in zip(coef, reversed(range(len(coef)))):
        sign = '+' if c > 0 else '-'
        digits_after_decimal_point = count_digits_after_decimal_point(c)
        result += "%s %.*f * X^%i " % (sign, digits_after_decimal_point, abs(c), i)
    return result + "= 0"
