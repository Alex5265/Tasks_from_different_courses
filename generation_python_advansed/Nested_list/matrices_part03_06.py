# Тренировка заполнения квадратных матриц.
# Задание на вход поступает длина стороны
# Необходимо создать матрицу, заполненную 0 в боковых четвертях, и 1 остальные значения

n = int(input())

matr = [[1 for j in range(n)] for i in range(n)]

# Согласно формуле приведенной в лекции у боковых вычислению боковых четвертей существует формула, тут она применяется.
for r in range(n):
    for c in range(n):
        if c > r > n - c - 1 or c < r < n - 1 - c:
            matr[r][c] = 0



for i in matr:
    print(*i)


# 7
# На выходе
# 1  1  1  1  1  1  1
# 0  1  1  1  1  1  0
# 0  0  1  1  1  0  0
# 0  0  0  1  0  0  0
# 0  0  1  1  1  0  0
# 0  1  1  1  1  1  0
# 1  1  1  1  1  1  1
#