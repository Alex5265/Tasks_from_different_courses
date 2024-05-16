# Реализуйте декоратор add_attrs, который принимает произвольное количество
# именованных аргументов и устанавливает их в качестве атрибутов декорируемой функции.
# Названием атрибута должно являться имя аргумента, значением атрибута — значение аргумента.
#
# Также декоратор должен сохранять имя и строку документации декорируемой функции.
#
# Примечание 1. Вспомните про атрибут функции __dict__.
#
# Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое
# значение декорируемой функции, а также должен уметь декорировать функции с произвольным
# количеством позиционных и именованных аргументов.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую только
# необходимый декоратор add_attrs, но не код, вызывающий его.
import functools

def add_attrs(**deckwargs):
    def decor(func):
        func.__dict__.update(deckwargs)
        return func
    return decor


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)




