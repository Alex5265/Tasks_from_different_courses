# Реализуйте класс Fibonacci, порождающий итераторы,
# конструктор которого не принимает никаких аргументов.
#
# Итератор класса Fibonacci должен генерировать бесконечную
# последовательность чисел Фибоначчи, начиная с 1.
#
# Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел,
# где каждое последующее число является суммой двух предыдущих:
# 1,1,2,3,5,8,13,21,34
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Fibonacci.

class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        return self.first



fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))













