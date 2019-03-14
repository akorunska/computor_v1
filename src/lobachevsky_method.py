from .custom_math import *

def quadr(n, a):
    b = []
    i = 0

    while i <= n:
        b.append(a[i] ** 2)
        j = 1
        added_val = 0
        while j <= n - i:
            if i - j >= 0:
                added_val += ((-1) ** j) * a[i - j] * a[i + j]
            j += 1
        b[i] += 2 * added_val
        i += 1
    return b


def norm_dist(n, a, b):
    dist = 0
    i = 0

    while i < n:
        if a[i] != 0:
            dist += (1 - b[i] / (a[i] ** 2)) ** 2
        i += 1
    return sqrt(dist)


def f(coefficients, x):
    value = 0
    for i in range(len(coefficients)):
        value += x ** i * coefficients[i]
    return value


def get_results(n, b, p, initial_coefficients):
    x = []
    i = 1

    while i <= n:
        val = (b[n - i] / b[n - i + 1]) ** (1 / 2 ** p)
        f_x = f(initial_coefficients, val)
        f_mx = f(initial_coefficients, -val)
        # print(val, f_x, f_mx)
        x.append(val if (abs(f_x) < abs(f_mx)) else -val)
        i += 1
    return x


# n учитывает индексацию с 0
def lobachevsky_method(n, a):
    initial_coefficients = a
    b = quadr(n, a)
    p = 1

    while norm_dist(n, a, b) > 0.8:
        print(a, "  =>\n", b, "\n\n")
        a = b
        b = quadr(n, a)
        p += 1

    return get_results(n, b, p, initial_coefficients)
