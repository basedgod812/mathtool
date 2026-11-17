import math

MAX_VALUE = 10000


def validate(a, b, c):
    if max(abs(a), abs(b), abs(c)) > MAX_VALUE:
        raise ValueError(f"error значение вне диапазона [{-MAX_VALUE};{MAX_VALUE}]")
    if a == 0 and b == 0:
        raise ValueError("error неизвестное отсутствует")


def solve(a, b, c):
    validate(a, b, c)
    if a == 0:
        return "линейное", None, [-c / b]

    d = b * b - 4 * a * c
    if d < 0:
        roots = []
    elif d == 0:
        roots = [-b / (2 * a)]
    else:
        roots = [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]
    return "квадратное", d, roots
