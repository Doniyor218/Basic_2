import statistics

try:
    x = list(map(int, input("Напечатайте множество чисел: ").split()))
    Cr = statistics.mean(x)
    Mo = statistics.multimode(x)
    Me = statistics.median(x)
    Di = statistics.pvariance(x)
    Ot = statistics.pstdev(x)
    print("Дисперсия:", Di)
    print("Медиана:", Me)
    print('Мода:', Mo)
    print("Среднее арифметическое:", Cr)
    print('Среднее отклонение:', O)
except (NameError):
    print('')
except (ValueError, TypeError):
    print("Пишите только числа!!!")