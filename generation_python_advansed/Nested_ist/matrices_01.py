# Тренировка составления и вывода двоичной матрицы.
# Задание на вход приходят количество рядов и столбцов затем данные.
# Необходимо внести данные в таблицу и вывести построчно


# принимаем количество рядов и столбцов
row, cols = int(input()), int(input())

# формируем пустую таблицу
mat = [[' '] * cols for i in range(row)]

# С помощью цикла принимаем по слову и добавляем в матрицу
for i in range(row):
    for j in range(cols):
        word = input()
        mat[i][j] = word

# С помощью цикла печатаем по ряду на строку
for c in mat:
    print(*c)

# 4
# 2
# и
# швец
# и
# жнец
# и
# на
# дуде
# игрец