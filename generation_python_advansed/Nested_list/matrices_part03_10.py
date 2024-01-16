# Тренировка заполнения матриц.
# Задание на вход поступает n и m количество строк и столбцов
# Необходимо заполнить матрицу "спиралью" крайне сложое задание

# Принимаем значение строк и столбцов для матрицы
n,m = [int(i) for i in input().split()]

# В данном случае специально заполняем нулями матрицу
matr = [[0 for j in range(m)] for i in range(n)]

# вводим переменные: i - значение, которое будет записываться в матрицу
# x, y текущие значения x- строки y - колонны, при этом в основном цикле мы как бы заглядываем
# с "-1" позиции в матрицу проверяем условия поэтому значение -1
i, x, y = 1, 0, -1

# Переменные которые могут принимать значения только -1 0 1 они указывают направление движения
# после проверки условий и т.к. змейка сначала двигается слева направо колоны начинаются с 1
row, col = 0, 1

# В цикле вайл происходит проверка переменной i как заполнителя матрицы, если она стала равной
# произведению колонн на ряды заполнение останавливается
while i <= n * m:
    # булиевая переменная которая проверяет границы движения по рядам,
    # играет ключевую роль только при проходе внешней границы матрицы
    row_status = 0 <= x + row < n
    # булиевая переменная которая проверяет границы движения по строкам,
    # играет ключевую роль только при проходе внешней границы матрицы
    colons_status = 0 <= y + col < m
    # Проверяем статус колон рядов и что следующий знак не равен 0,
    # это условие крайне важно т.к. после похода внешнего круга поворот по спирали происходит
    # только из-за последнего условия
    if row_status and colons_status and matr[x + row][y + col] == 0:
        x += row
        y += col
        matr[x][y] = i
        i += 1
    # Если булевы условия не соблюдаются то происходит смена направления, при этом движение по спирали строгое
    # и мы можем задать условия после движения слева-направо необходимо двигаться сверху-вниз
    # поэтому переменая двигающая колонны - 0 а ряды -1
    elif col == 1:
        col = 0
        row = 1
    # после движения сверху-вниз всегда строго необходимо двигаться справа-налево
    # поэтому ряды 0 колонны -1
    elif row == 1:
        row = 0
        col = -1
    # Затем всегда строго необходимо двигаться снизу-вверх
    # поэтому колоны 0 ряды -1
    elif col == -1:
        col = 0
        row = -1
    # И всегда строго при несоблюдении условий поворачиваем движение слева-направо
    elif row == -1:
        row = 0
        col = 1


for i in range(n):
    for j in range(m):
        print(str(matr[i][j]).ljust(3), end="")
    print()