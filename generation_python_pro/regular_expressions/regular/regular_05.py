# Напишите программу, определяющую:
#
# количество строк, в которых bee встречается в качестве подстроки не менее двух раз
# количество строк, в которых geek встречается в качестве слова хотя бы один раз
# Формат входных данных
# На вход программе произвольное количество строк, каждая из которых содержит набор произвольных символов.
#
# Формат выходных данных
# Программа должна вывести два числа:
#
# первое — количество строк, в которых bee встречается в качестве подстроки не менее двух раз
# второе — количество строк, в которых geek встречается в качестве слова хотя бы один раз
# каждое на отдельной строке.
#
# Примечание 1. Словом будем считать любую непрерывную последовательность из одного или нескольких символов, соответствующих \w.
#
# Примечание 2. Строка может одновременно удовлетворять обоим условиям.
#
# Примечание 3. В первой строке первого теста bee встречается в качестве подстроки
# 3
# 3 раза:
#
# beebee bee
# Во второй строке bee встречается в качестве подстроки лишь один раз, а слово geek отсутствует.
#
# В третьей строке bee встречается в качестве подстроки
# 2
# 2 раза, geek в качестве слова —
# 1
# 1 раз:
#
# bee geek bee
from re import search


regex_bee = r'(bee).*(bee)'
regex_geek = r'\b(geek)\b'

words =[i.strip() for i in open(0)]

print(sum( ( bool(search(regex_bee, i)) for i in words) ))
print(sum( ( bool(search(regex_geek, i)) for i in words) ))















