# Напишите программу, которая разбивает строку по символам точки,
# запятой и точки с запятой.
#
# Формат входных данных
# На вход программе подается строка, содержащая различные значения, разделенные
# символами точки ., запятой , или точки с запятой ;, вокруг которых могут располагаться пробелы.
#
# Формат выходных данных
# Программа должна разбить введенную строку по символам точки, запятой и точки
# с запятой, захватывая вокруг стоящие пробелы, и вывести все значения,
# полученные при разбиении, через пробел.

import re

result = re.split(r'\s*[,;.]\s*', input())

print(result)
