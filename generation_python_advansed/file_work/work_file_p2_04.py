# Вам доступен текстовый файл numbers.txt, каждая строка которого может
# содержать одно или несколько целых чисел, разделенных одним или
# несколькими пробелами.
# Напишите программу, которая вычисляет сумму чисел в каждой строке и
# выводит эту сумму на экран (для каждой строки выводится сумма чисел в этой строке).
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна вывести сумму чисел в каждой строке.



with open('numbers_p2_04.txt', 'rt', encoding='utf-8') as numbers:
    for line in numbers:
        print(sum([int(i) for i in line.split()]))





# Примечание 1. Если бы файл numbers.txt содержал строки:
#
# 2 1
#      3    40
#  10       7
# то результатом было бы:
#
# 3
# 43
# 17