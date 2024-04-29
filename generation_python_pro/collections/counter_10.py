# Дан список имен учеников и их оценок за экзамен.
# Напишите программу, которая определяет второго по счету ученика, имеющего самую низкую оценку.
#
# Формат входных данных
# На вход программе подается произвольное количество строк,
# в каждой из которых записаны имя очередного ученика и его оценка, разделенные пробелом.
#
# Формат выходных данных
# Программа должна определить второго по счету ученика,
# который имеет самую низкую оценку, и вывести его имя.
#
# Примечание 1. Гарантируется, что все ученики имеют различные имена и оценки.

import sys

data = [ tuple(row.strip().split()) for row in sys.stdin]

print(sorted(data, key=lambda x: int(x[1]))[1][0])









