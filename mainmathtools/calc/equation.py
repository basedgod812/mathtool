import math

MAX_VALUE = 10000


def valid(a, b, c):
    if max(abs(a), abs(b), abs(c)) > MAX_VALUE:
        raise ValueError(f"error значение вне диапазона [{-MAX_VALUE};{MAX_VALUE}]")
    if a == 0 and b == 0:
        raise ValueError("error неизвестное отсутствует")

def solve(a, b, c):
    """Вернуть вид уравнения, дискриминант и список корней."""
    valid(a,b,c)
    if a == 0:#Ax^2 пропал, bx + c = 0
        return "линейное", None, [-c / b] #none=нет D
    d = b * b - 4 * a * c
    if d < 0:
        korni = []
    elif d == 0:
        korni = [-b / (2 * a)]
    else:
        korni = math.sqrt(d)
        korni = [(-b - korni) / (2 * a), (-b + korni) / (2 * a)]
    return "квадратное", d,korni

