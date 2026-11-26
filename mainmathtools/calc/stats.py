import math

MAX_COUNT = 20
MAX_ABS = 10000


def parse_numbers(lines):
    """Прочитать числа и проверить, подходят ли они."""
    numbers = []

    for line in lines:
        for word in line.split():
            try:
                value = float(word)
            except ValueError:
                raise ValueError(f"{word} не является числом") from None

            if not math.isfinite(value):#проверяет что число конечное
                raise ValueError("число должно быть конечным")

            if abs(value) > MAX_ABS:
                raise ValueError("число вне диапазона от -10000 до 10000")

            if len(numbers) == MAX_COUNT:
                raise ValueError("можно ввести не больше 20 чисел")

            numbers.append(value)

    if not numbers:
        raise ValueError("список чисел пуст")

    return numbers

def total(numbers):
    """Найти сумму чисел."""
    result = 0.0

    for number in numbers:
        result += number

    return result

def mean(numbers):
    """Найти среднее арифметическое."""
    return total(numbers) / len(numbers)

def minimum(numbers):
    """Найти наименьшее число."""
    return min(numbers)

def maximum(numbers):
    """Найти наибольшее число."""
    return max(numbers)

def positives(numbers):
    """Посчитать положительные числа."""
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count

def negatives(numbers):
    """Посчитать отрицательные числа."""
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count