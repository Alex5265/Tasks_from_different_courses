# Как известно, функция map() принимает функцию и итерируемый объект и возвращает итератор,
# элементами которого являются элементы итерируемого объекта, к которым была применена переданная функция.
# Нередко элементами итерируемого объекта являются коллекции (списки, кортежи, ..),
# тогда внутри переданной функции нам приходится обращаться к каждому элементу этих коллекций по индексу.
# Например:
#
# persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
#
# full_names = map(lambda tup: tup[0] + ' ' + tup[1], persons)
# Было бы удобно иметь функцию, назовем ее starmap(), которая бы принимала функцию не с
# одним аргументом, а с несколькими — каждым элементом коллекции:
#
# persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
#
# full_names = starmap(lambda name, surname: f'{name} {surname}', persons)
# Реализуйте функцию starmap() с использованием функции map(), которая принимает два аргумента:
#
# func — функция
# iterable — итерируемый объект, элементами которого являются коллекции
# Функция starmap() должна работать аналогично функции map(), то есть возвращать итератор,
# элементами которого являются элементы итерируемого объекта iterable,
# к которым была применена функция func, с единственным отличием:
# func должна принимать не один аргумент — коллекцию (элемент iterable),
# а каждый элемент этой коллекции в качестве самостоятельного аргумента.


def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)


pairs = [(1, 3), (2, 5), (6, 4)]

print(*starmap(lambda a, b: a + b, pairs))














