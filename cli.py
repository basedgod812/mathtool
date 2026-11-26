import argparse #чтение команд терминала
def build_parser():
    """Описать команду solve и её параметры."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="Решение уравнений",
    )
    command = parser.add_subparsers(dest="command") #место для команд

    solve = command.add_parser("solve", help="Решить уравнение")
    solve.add_argument("-a", type=int, help="Коэффициент A")
    solve.add_argument("-b", type=int, help="Коэффициент B")
    solve.add_argument("-c", type=int, help="Коэффициент C")

    return parser
