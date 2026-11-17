#импорт библиотек
import sys
from calc import equation

#список аргументов командной строки
args = sys.argv[1:]
#вывод справки
if len(args) == 0 or args[0] == "--help":
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print(f"Коэффициенты A, B, C — целые числа, по модулю не превышающие {equation.MAX_VALUE}.")
    sys.exit(0) 

if args[0] != "solve":
    sys.exit("error неизвестная команда")
#ввод переменной если условия соблюдены
if len(args) == 1:
    values = [input("Введите A: "), input("Введите B: "), input("Введите C: ")]
elif len(args) == 7:
    if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
        sys.exit("error неизвестный параметр")
    values = [args[2], args[4], args[6]]
else:
    sys.exit("error неверный набор параметров")

#Преобразование в целые числа
try:
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
except ValueError:
    sys.exit("error коэффициент не является целым числом")

try:
    kind, d, roots = equation.solve(a, b, c)
except ValueError as error:
    sys.exit(str(error))

print(f"Уравнение {kind}")
if kind == "линейное":
    print(f"x = {roots[0]}")
else:
    print(f"D = {d}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("корней нет")
