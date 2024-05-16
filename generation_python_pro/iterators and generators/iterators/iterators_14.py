# Реализуйте класс Repeater, порождающий итераторы,
# конструктор которого принимает один аргумент:
#
# obj — произвольный объект
# Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.
#
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимый класс Repeater.

class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))













