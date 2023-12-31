# Тренировка матриц.
# Задание необходимо обменять местами занчения диагоналей, оставляя значения в том же столбце

# получаем количество строк и столбцов в талице
n = int(input())
# вносим полученные данные через сплит строк
matr = [[int(i) for i in input().split()] for j in range(n)]

# меняем местами согласно выявленной закономерности
for i in range(n):
    matr[i][n -1 - i], matr[n - i - 1][n - i - 1] = matr[n - i - 1][n - i - 1], matr[i][n -1 - i]

#выводим полученый результат
for el in matr:
    print(*el)

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# На выходе
# 7 2 9
# 4 5 6
# 1 8 3

#Визуализация закономерностей индексов
# 0,0  0,1  0,2  0,3
# 1,0  1,1  1,2  1,3
# 2,0  2,1  2,2  2,3
# 3,0  3,1  3,2  3,3