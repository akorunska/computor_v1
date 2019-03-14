
def abs(val):
    if val < 0:
        return -1 * val
    return val


def sqrt(val):
    if val < 0:
        return 0
    eps = 0.00000001
    current_value = abs(val)
    prev_value = 0
    while abs(prev_value - current_value) > eps:
        prev_value = current_value
        current_value = 1 / 2 * (current_value + abs(val) / current_value)
    return current_value
