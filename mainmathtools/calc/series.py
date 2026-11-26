import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000
DIGITS = math.ceil(-math.log10(MAX_EPS))

def sign(n):
    """вернуть знак слагаемого с номером n."""
    return -1 if n % 2 == 0 else 1

def third(n):
    """вычислить слагаемое ряда third."""
    return sign(n) / (3 * n)

def sqplus(n):
    """вычислить слагаемое ряда sqplus."""
    return sign(n) / (n * n + 1)

FORMULAS = {
    "third": (third, "S = 1/3 - 1/6 + 1/9 - ..."),
    "sqplus": (sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
}

def sum_by_count(term, count):
    """сложить заданное число слагаемых."""
    if not 1 <= count <= MAX_TERMS:
        raise ValueError("количество слагаемых вне диапазона")
    
    result = 0.0
    for n in range(1, count + 1):
        result += term(n)

    return result, count

def sum_by_eps(term, eps):
    """сложить ряд до первого достаточно малого слагаемого."""
    if not 0 < eps <= MAX_EPS:
        raise ValueError("точность вне диапазона")

    result = 0.0
    for n in range(1, MAX_ITERATIONS + 1):
        value = term(n)
        result += value

        if abs(value) < eps:
            return result, n

    raise ValueError("точность не достигнута")