# Как известно, во время итерации по словарю мы получаем ключи,
# а не значения или пары ключ-значение.
#
# Приведенный ниже код:
#
# info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}
#
# print(*info)
# выводит:
#
# name age gender
# Реализуйте класс DictItemsIterator, порождающий итераторы,
# конструктор которого принимает один аргумент:
#
# data — словарь
# Итератор класса DictItemsIterator должен генерировать последовательность кортежей,
# представляющих собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.
#
# Примечание 1. При решении задачи не используйте словарные методы keys(), values() и items().
#
# Примечание 2. Пары ключ-значение в возвращаемом функцией итераторе
# должны располагаться в своем изначальном порядке.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую
# только необходимый класс DictItemsIterator.


class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self.keys)
        return val, self.data[val]


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)














