# Реализуйте функцию get_min_max(), которая принимает один аргумент:
#
# data — список произвольных объектов, сравнимых между собой
# Функция должна возвращать кортеж, в котором первым элементом является индекс
# минимального элемента в списке data, вторым — индекс максимального элемента в списке data.
# Если список data пуст, функция должна вернуть значение None.
#
# Примечание 1. Если минимальных / максимальных элементов несколько, следует вернуть
# индексы первого по порядку элемента.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только
# необходимую функцию get_min_max(), но не код, вызывающий ее.


def get_min_max(data):
    if data:
        res_min = data.index(min(data))
        res_max = data.index(max(data))
        return (res_min, res_max)


data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))











