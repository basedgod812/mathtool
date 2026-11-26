import argparse

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

    stats = command.add_parser("stats", help="Посчитать статистику")#команта статс
    stats.add_argument("--input", help="Файл с числами")#можно указать файл с числами

    return parser
