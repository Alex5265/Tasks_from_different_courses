# Тренировка составления и вывода двоичной матрицы.
# Задание на вход приходят длина строк и столбцов.
# Необходимо вывести таблицу умножения при этом добавить метод выравнивания строк (3 символа)


n, m = int(input()), int(input())
matr = []

for r in range(n):
    row = []
    for c in range(m):
        row.append(str(r * c).ljust(3))
    matr.append(row)

for el in matr:
    print(*el)


# 4
# 6
# НА выходе
# 0  0  0  0  0  0
# 0  1  2  3  4  5
# 0  2  4  6  8  10
# 0  3  6  9  12 15
