# Методы множеств
# На выход поступают балы по 10 бальной шкале. Поступает 3 строки баллов разделенные пробелами
# необходимо вывести множество оценок которые есть и у первого и второго ученика, но нет у третьего


set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())

set4 = set1 & set2 - set3

print(*sorted(set4, key=int, reverse=True))