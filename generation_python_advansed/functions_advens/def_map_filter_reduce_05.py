# Напишите функцию func_apply(),
# принимающую на вход функцию и список значений и возвращающую список,
# в котором каждое значение будет результатом применения
# переданной функции к переданному списку.


# по факту от нас требуют написать функцию мар.
def func_apply(funct, iter):
    result = []
    for it in iter:
        result.append(funct(it))
    return result







def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))

#  Примечание 1. Приведенный ниже код, при условии, что функция func_apply() написана правильно
# def add3(x):
#     return x + 3
#
# def mul7(x):
#     return x * 7
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))
# должен выводить:
#
# [7, 14, 21, 28, 35, 42]
# [4, 5, 6, 7, 8, 9]
# ['1', '2', '3', '4', '5', '6']