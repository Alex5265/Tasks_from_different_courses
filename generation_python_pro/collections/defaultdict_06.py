# Реализуйте функцию flip_dict(), которая принимает один аргумент:
#
# dict_of_lists — словарь, в котором ключом является число или строка, а значением — список чисел или строк
# Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве значения по умолчанию), который представляет собой «перевернутый» словарь dict_of_lists.
#
# Примечание 1. Ключи в возвращаемом функцией словаре, а также элементы в списках должны располагаться в своем исходном порядке.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию flip_dict(), но не код, вызывающий ее.
#
# Примечание 3. Тестовые данные доступны по ссылкам:

from collections import defaultdict

def flip_dict(dict_of_lists):
    def_dict = defaultdict(list)

    for k, v in dict_of_lists.items():
        for el in v:
            def_dict[el].append(k)
    return def_dict



print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))








