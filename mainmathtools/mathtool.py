#импорт библиотек
import sys

from calc import equation, stats, series, integrate
from cli import build_parser

def handle_solve(args):
    """получить коэффициенты и показать решение."""
    a, b, c = args.a, args.b, args.c
    if a is None and b is None and c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except (ValueError, EOFError):
            raise ValueError("error коэффициент не является целым числом") from None
    elif a is None or b is None or c is None:
        raise ValueError("укажите три коэффициента либо ниолдного")
    kind, d, korni = equation.solve(a, b, c)

    print(f"Уравнение {kind}")

    if d is not None:
        print(f"D = {d}")

    if len(korni) == 2:
        print(f"x1 = {korni[0]:.3f}")
        print(f"x2 = {korni[1]:.3f}")
    elif len(korni) == 1:
        print(f"x = {korni[0]:.3f}")
    else:
        print("корней нет")

def handle_stats(args):
    """прочитать числа из файла или с клавиатуры."""
    if args.input is None:
        numbers = stats.parse_numbers(sys.stdin)
    else:
        try:
            with open(args.input, encoding="utf-8-sig") as source:
                numbers = stats.parse_numbers(source)
        except OSError:
            raise ValueError("не удалось открыть файл с числами") from None

    for label, function, form in stats.INDICATORS:
        value = function(numbers)

        if value is None:
            text = "НЕ СУЩЕСТВУЕТ"
        else:
            text = format(value, form)

        print(f"{label}: {text}")

def handle_series(args):
    """рассчитать и вывести сумму выбранного ряда."""
    term, formula = series.FORMULAS[args.func]

    if args.terms is None:
        result, count = series.sum_by_eps(term, args.eps)
    else:
        result, count = series.sum_by_count(term, args.terms)

    print(formula)
    print(f"слагаемых: {count}")
    print(f"сумма ряда: {result:.{series.DIGITS}f}")

def handle_integrate(args):
    """проверить данные, вычислить интеграл и показать результат."""
    function, formula, lower, upper, closed = integrate.FUNCTIONS[args.func]

    integrate.validate(args.lower, args.upper, args.steps, lower, upper, closed)
    result = integrate.integrate(function, args.lower, args.upper, args.steps)

    print(formula)
    print(f"значение интеграла: {result:.4f}")

HANDLERS = {
        "solve": handle_solve,
        "stats": handle_stats,
        "series": handle_series,
        "integrate": handle_integrate,
    }
def main():
    """разобрать команду и запустить её обработчик."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    try:
        HANDLERS[args.command](args)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    return 0
if __name__ == "__main__":
    sys.exit(main())