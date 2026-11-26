# mathtool
Лабораторная работа № 2 «Обработка числовых рядов».

## Команды

```bash
python3 mathtool.py solve -a 1 -b -3 -c 2
python3 mathtool.py stats --input numbers.txt
python3 mathtool.py series --func sqplus --terms 6
python3 mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000
```

- `solve` решает уравнение. Если запустить без коэффициентов, программа спросит их с клавиатуры.
- `stats` считает статистику по числам из файла или стандартного ввода.
- `series` считает сумму ряда по количеству слагаемых или до заданного порога.
- `integrate` приближённо вычисляет интеграл методом левых прямоугольников.

Общая справка открывается командой `python3 mathtool.py --help`.
Для справки по отдельной команде, например `series`, 
`python3 mathtool.py series --help`.