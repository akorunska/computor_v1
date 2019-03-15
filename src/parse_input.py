import re
from .custom_math import *

pattern = r"((^[-+ ]?|[-+])[\s]*([0-9]+[\s]*\*?[/s]*[\s]*)?X([\s]*\^[\s]*[0-9]+)?)|([-+]?[\s]*[0-9]+)"


def get_max_equation_pow(result):
    max_pow = 0
    for r in result:
        # print(r)
        full, sign, coef, pow, free = r
        cur_pow = 0
        if coef == '' and pow == '' and free == '':
            cur_pow = 1
        elif free != '':
            cur_pow = 0
        elif pow != '':
            cur_pow = int(re.findall(r'\^[\s]*([0-9]+)', pow)[0])
        if cur_pow > max_pow:
            max_pow = cur_pow
    return max_pow


def parse_coefficients(input_str: str, max_pow):
    result = re.findall(pattern, input_str)

    l = [0] * (max_pow + 1)
    for r in result:
        full, sign, coef, pow, free = r
        sign_multiplier = -1 if sign.replace(" ", "") == '-' else 1

        if free == '':
            cur_pow = 1
            if pow != '':
                cur_pow = int(re.findall(r'\^[\s]*([0-9]+)', pow)[0])
            if coef == '':
                l[cur_pow] += 1 * sign_multiplier
            else:
                c = re.findall(r'([0-9]+)\*?', coef.replace(" ", ""))[0]
                l[cur_pow] += int(c) * sign_multiplier
        else:
            l[0] += int(free.replace(" ", ""))
    return l


def validate_equation(input_str):
    results = re.findall(pattern, input_str)
    recognised = "".join(line[0] if line[0] != '' else line[4] for line in results).replace(" ", "")
    j = 0
    for i in range(len(input_str)):
        if input_str[i] != ' ':
            if j >= len(recognised):
                return i
            if input_str[i] != recognised[j]:
                return i
            j += 1
    return -1


def check_input(eq_parts: list):
    if len(eq_parts) != 2:
        return "No or too many '=' found"
    for p in eq_parts:
        if p.replace(" ", "") == "":
            return "Part of equation can not be left blank"
    index_right = validate_equation(eq_parts[0])
    if index_right >= 0:
        return (
            "%s\n" % (eq_parts[0] + "=" + eq_parts[1]) +
            " " * index_right + "^\n"
            "Unrecognised symbol '%s' at index %i" % (eq_parts[0][index_right], index_right)
        )
    index_left = validate_equation(eq_parts[1])
    if index_left >= 0:
        return (
            "%s\n" % (eq_parts[0] + "=" + eq_parts[1]) +
            " " * (index_left + len(eq_parts[0]) + 1) + "^\n"
            "Unrecognised symbol '%s' at index %i" % (eq_parts[1][index_left], index_left + len(eq_parts[0]) + 1)
        )
    return False


def parse_input(input_str: str):
    eq_parts = input_str.split('=')
    error = check_input(eq_parts)
    if error != False:
        return error

    max_pow = max(get_max_equation_pow(re.findall(pattern, input_str)), 2)
    right = parse_coefficients(eq_parts[0], max_pow)
    left = parse_coefficients(eq_parts[1], max_pow)

    for i in range(max_pow + 1):
        right[i] -= left[i]
    return list(reversed(right))

