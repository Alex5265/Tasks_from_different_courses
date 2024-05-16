# Реализуйте декоратор takes_positive, который проверяет, что все аргументы,
# передаваемые в декорируемую функцию, являются положительными целыми числами.
#
# Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
#
# TypeError, если аргумент не является целым числом
# ValueError, если аргумент является целым числом, но отрицательным или равным нулю
# Примечание 1. Приоритет возбуждения исключений при несоответствии
# аргумента обоим условиям или при наличии разных аргументов, несоответствующих разным условиям:
# TypeError, затем ValueError.
#
# Примечание 2. Не забывайте про то, что декоратор не должен поглощать
# возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 3. В тестирующую систему сдайте программу,
# содержащую только необходимый декоратор takes_positive, но не код, вызывающий его.


def takes_positive(func):
    def wrapper(*args, **kwargs):
        if not all(type(i) is int for i in (*args, *kwargs.values())):
            raise TypeError
        elif not all(i > 0 for i in (*args, *kwargs.values())):
            raise ValueError
        else:
            return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))





