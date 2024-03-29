# Напишите программу, которая сортирует список points координат точек
# плоскости в соответствии с расстоянием от начала координат (точки (0;0)).
# Программа должна вывести отсортированный список.
# Примечание. Расстояние от начала координат O(0;0) до точки A(x;y) =
# x**2+y**2 извлечь корень из результата


# Функция сорт, как и другие некоторые функции в качестве ключа могут принимать функции
# в данном случае условие записываем в функцию и т.к. начало координат - 0 0
# то значения автоматически сортируются как необходимо
def calculate_distance(point):
    x, y = point
    return (x**2 + y**2) ** 0.5




points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0),
          (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]





print(sorted(points, key=calculate_distance))