import argparse
from calc import series, integrate

def build_parser():
    """Описать команду solve и ее параметры"""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description = "решение уравнений"
    )
    command = parser.add_subparsers(dest="command")#создает место для команд

    solve = command.add_parser("solve", help="Rешить уравнение")
    solve.add_argument("-a", type=int, help="коэффициент A")
    solve.add_argument("-b", type=int, help="коэффициент B")
    solve.add_argument("-c", type=int, help="коэффициент C")

    stats = command.add_parser("stats", help="Посчитать статистику", allow_abbrev=False)#команта статс
    stats.add_argument("--input", help="Файл с числами")#можно указать файл с числами

    series_command = command.add_parser(
        "series", help="Найти сумму ряда", allow_abbrev=False
    )
    series_command.add_argument(
        "--func", required=True, choices=sorted(series.FORMULAS), help="Название ряда"
    )
    stop = series_command.add_mutually_exclusive_group(required=True)
    stop.add_argument("--terms", type=int, help="Количество слагаемых")
    stop.add_argument("--eps", type=float, help="Точность суммирования")

    integral = command.add_parser(
        "integrate", help="Вычислить интеграл", allow_abbrev=False
    )
    integral.add_argument(
        "--func", required=True, choices=sorted(integrate.FUNCTIONS),
        help="Имя функции"
    )
    integral.add_argument(
        "--from", dest="lower", required=True, type=float, help="Начало промежутка"
    )
    integral.add_argument(
        "--to", dest="upper", required=True, type=float, help="Конец промежутка"
    )
    integral.add_argument(
        "--steps", required=True, type=int, help="Число прямоугольников"
    )
    return parser
