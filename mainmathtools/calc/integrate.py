import math

MAX_STEPS = 100000


def ratio(x):
    """вычислить x / (x + 1)."""
    return x / (x + 1)


def root(x):
    """вычислить квадратный корень из x² + 1."""
    return math.sqrt(x * x + 1)


FUNCTIONS = {
    "ratio": (ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}


def validate(a, b, steps, lower, upper, closed):
    """проверить границы и количество шагов."""
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("предел должен быть конечным числом")

    if a >= b:
        raise ValueError("начальный предел не меньше конечного")

    if a < lower or b > upper or (not closed and (a == lower or b == upper)):
        raise ValueError("предел вне промежутка")

    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")


def integrate(function, a, b, steps):
    """сложить площади прямоугольников по значениям на левом краю."""
    dx = (b - a) / steps
    result = 0.0

    for i in range(steps):
        x = a + i * dx
        result += function(x) * dx

    return result