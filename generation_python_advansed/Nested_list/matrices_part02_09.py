# Тренировка матриц.
# Задание необходимо проверить квадратную таблицу, является ли она магическим квадратом.
# (сумма значений в столбцах, строках, и диагоналях равны между собой)


# Получаем длину символов
n = int(input())

# Через сплин добавляем int в таблицу
matr = [[int(i) for i in input().split()] for j in range(n)]

#присваиваем переменной значение ответа "да"
answer = 'YES'
# формируем лист чисел который должен быть в магическом квадрате
need_num = list(range(1,n**2 + 1))
#формируем пустой лист числе которые у нас будут встречаться фактически
factical_num = []

# т.к. матрица квадратная всю проверку по строкам и диагоналям возможно провести
# в одном для проверки всех столбцов необходимо вложенный цикл, поэтому создается 2 цикла в котором
# происходит подсчет (возможный недочет) n раз считаются диагонали и сумма каждого стоблца и строки
# а затем сравниваются между собой
for r in range(n):
    # значение главной диагнонали
    m_diag = 0
    # значение дополнительной диагонали
    d_diag = 0
    # значение строки
    row_sum = 0
    # значение столбца
    colon_sum = 0
    for c in range(n):
        # для проверки сравниваем число матрицы с числами которые должны быть
        if matr[r][c] not in need_num:
            #если такого значения нет (что не может быть) то значени добавляется в список
            need_num.append(matr[r][c])
        # для проверки сравниваем число матрицы с числами фактически присутствуют
        if matr[r][c] not in factical_num:
            # если такогозначения нет, то добавляем в список
            factical_num.append(matr[r][c])
        # вычисляется сумма главной диагонали
        m_diag += matr[c][c]
        #вычисляется сумма дополнительной диагонали
        d_diag += matr[c][n - c - 1]
        # высисляется сумма ряда
        row_sum += matr[r][c]
        #вычисляется сумма столбца
        colon_sum += matr[n - c - 1][r]

    #если сумма диагоналей не совпадает или сумма строк и столбцов не совпадает ответ равен "нет"
    if (m_diag != d_diag) or (row_sum != colon_sum):
        answer = 'NO'
        break

# если длина нужный цифр и фактических не совпадает, так же ответу присваивается нет.
if len(need_num) != len(factical_num):
    answer = 'NO'


print(answer)


# 3
# 8 1 6
# 3 5 7
# 4 9 2
# На выходе
# YES
#
#
# 3
# 8 2 6
# 3 5 7
# 4 9 1
# На выходе
# NO
#
#
#