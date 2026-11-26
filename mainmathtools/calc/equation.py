import math

MAX_VALUE = 10000

def valid(a, b, c):
    for name, value in {"A": a, "B": b, "C": c}.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")
    if a == 0 and b == 0:
        raise ValueError("error неизвестное отсутствует")

def solve(a, b, c):
    """вернуть вид уравнения, дискриминант и список корней."""
    valid(a, b, c)
    if a == 0:  # Ax^2 пропал, bx + c = 0
        return "линейное", None, [-c / b]  # none=нет D
    d = b * b - 4 * a * c
    if d < 0:  # корней нет
        korni = []
    elif d == 0:  # один корень
        korni = [-b / (2 * a)]
    else:  # два корня
        root = math.sqrt(d)
        korni = [(-b + root) / (2 * a), (-b - root) / (2 * a)]
    return "квадратное", d,korni

