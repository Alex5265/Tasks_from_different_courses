# Методы множеств
# На выход поступают балы по 10 бальной шкале. Поступает 3 строки баллов разделенные пробелами
# необходимо вывести множество оценок, не встречающихся ни у одного их трех учеников.

set1, set2, set3 = set(input().split()), set(input().split()), set(input().split())

set4 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'} - set1 - set2 - set3

print(*sorted(set4, key=int))