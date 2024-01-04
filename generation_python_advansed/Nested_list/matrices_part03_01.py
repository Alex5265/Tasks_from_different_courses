# Тренировка заполнения матриц.
# Задание на вход поступаю два натуральнх числа n и m
# необходимо заполнить её символами "." и "*" в шахматном порядке

# получаем значение столбцов и строк
n, m = [int(i) for i in input().split()]

# заполняем матрицу знаками '*' с нужными параметрами
chest_table = [['*'] * m for i in range(n)]

# Во втором вложенном цикле происходит ключевая вещь - вычисляется остаток от деления на 2 от r
# т.е там поочередно будет или 0 или 1 и потом с шагом 2 заполняется знаком "." таблица поэтому выходит в шахматном порядке
for r in range(n):
    for c in range(r % 2, m, 2):
        chest_table[r][c] = '.'


# выводим получившуюся таблицу
for el in chest_table:
    print(*el)


# 8 8
# На выходе
#
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
# . * . * . * . *
# * . * . * . * .
