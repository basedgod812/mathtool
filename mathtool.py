import sys
import math

MAX_VALUE = 10000

# 1. Разбор параметров командной строки
args = sys.argv[1:]

if len(args) == 0 or args[0] == "--help":
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print("Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.")
    sys.exit(0)

if args[0] != "solve":
    sys.exit("error неизвестная команда")

if len(args) == 1:
    values = [input("Введите A: "), input("Введите B: "), input("Введите C: ")]
elif len(args) == 7:
    if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
        sys.exit("error неизвестный параметр")
    values = [args[2], args[4], args[6]]
else:
    sys.exit("error неверный набор параметров")

# 2. Преобразование в целые числа
try:
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
except ValueError:
    sys.exit("error коэффициент не является целым числом")

# 3. Проверка диапазона
if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    sys.exit("error значение вне диапазона")

# 4. Решение
if a == 0:
    if b == 0:
        sys.exit("error неизвестное отсутствует")
    print("Уравнение линейное")
    print(f"x = {-c / b:.3f}")
else:
    print("Уравнение квадратное")
    d = b * b - 4 * a * c
    print(f"D = {d}")
    if d > 0:
        print(f"x1 = {(-b + math.sqrt(d)) / (2 * a):.3f}")
        print(f"x2 = {(-b - math.sqrt(d)) / (2 * a):.3f}")
    elif d == 0:
        print(f"x = {-b / (2 * a):.3f}")
    else:
        print("корней нет")
