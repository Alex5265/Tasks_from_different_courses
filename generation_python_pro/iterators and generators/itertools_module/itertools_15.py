# Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# n — натуральное число
# Функция должна возвращать итератор, генерирующий последовательность,
# элементами которой являются объединенные в кортежи по n элементов
# соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей,
# то ими становится значение None.
#
# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией
# итераторе должны располагаться в своем исходном порядке.
#
# Примечание 2. Гарантируется, что итерируемый объект, передаваемый
# в функцию, не является множеством.
#
# Примечание 3. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию grouper(), но не код, вызывающий ее.
from itertools import zip_longest


def grouper(iterable, n):
    iterable = iter(iterable)
    return zip_longest(*[iterable for _ in range(n)])



iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))













