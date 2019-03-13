from .ComplexNumber import ComplexNumber


def count_discriminant(a, b, c):
    return b**2 - 4 * a * c


def get_two_complex_numbers_result(a, b, c, d):
    d_sqrt1, d_sqrt2 = ComplexNumber.sqrt(d)

    return [(d_sqrt1 - b) / 2*a, (d_sqrt2 - b) / 2*a]


def get_one_real_number_result(a, b, c, d):
    d_sqrt = ComplexNumber.sqrt(d)

    x = (-b + d_sqrt) / 2 * a
    return [x]


def get_two_real_numbers_result(a, b, c, d):
    d_sqrt = ComplexNumber.sqrt(d)

    x1 = (-b - d_sqrt) / 2 * a
    x2 = (-b + d_sqrt) / 2 * a
    return [x1, x2]


def get_discriminant_conclusions(d: float):
    print("D = ", d)

    if d < 0:
        print("Discriminant strictly negative, getting answer as two complex numbers:")
        return get_two_complex_numbers_result
    if d == 0:
        print("Discriminant is zero, getting one answer as real number:")
        return get_one_real_number_result
    if d > 0:
        print("Discriminant strictly positive, getting answer as two real numbers:")
        return get_two_real_numbers_result


def solve_quadratic_equation(a, b, c):
    d = count_discriminant(a, b, c)
    get_result = get_discriminant_conclusions(d)
    answers = get_result(a, b, c, d)
    for a in answers:
        print(a)


