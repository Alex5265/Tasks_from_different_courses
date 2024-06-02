# Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна заменять все множественные пробелы в строке
# string на единственный пробел и возвращать полученный результат.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую
# только необходимую функцию normalize_whitespace(), но не код, вызывающий ее.
import re


def normalize_whitespace(string):
    regex = r' {2,}'
    return re.sub(regex, r' ', string)




print(normalize_whitespace('AAAA                A                AAAA'))








