import re
# ([-+]?[\s]*([0-9]+[\s]*\*[/s]*[\s]*)?X([\s]*\^[\s]*[0-9]+)?)|([-+]?[\s]*[0-9])

pattern = r"(([-+]?)[\s]*([0-9]+[\s]*\*?[/s]*[\s]*)?X([\s]*\^[\s]*[0-9]+)?)|([-+]?[\s]*[0-9]+)"

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


def parse_input(input_str: str):
    eq_parts = input_str.split('=')
    if len(eq_parts) != 2:
        return "No '=' found"
    max_pow = get_max_equation_pow(re.findall(pattern, input_str))
    right = parse_coefficients(eq_parts[0], max_pow)
    left = parse_coefficients(eq_parts[1], max_pow)

    for i in range(max_pow + 1):
        right[i] -= left[i]
    return list(reversed(right))

