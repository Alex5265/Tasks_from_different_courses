# В различных социальных сетях существуют системы лайков,
# которые в зависимости от количества людей, оценивших запись,
# показывают соответствующую информацию.
#
# Реализуйте функцию likes(), которая принимает один аргумент:
#
# names — список имён
# Функция должна возвращать строку в соответствии с примерами ниже,
# содержание которой зависит от количества имён в списке names.
#
# Приведенный ниже код:
#
# print(likes([]))
# print(likes(['Тимур']))
# print(likes(['Тимур', 'Артур']))
# print(likes(['Тимур', 'Артур', 'Руслан']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
# должен выводить:
#
# Никто не оценил данную запись
# Тимур оценил(а) данную запись
# Тимур и Артур оценили данную запись
# Тимур, Артур и Руслан оценили данную запись
# Тимур, Артур и 2 других оценили данную запись
# Тимур, Артур и 3 других оценили данную запись
# Тимур, Артур и 6 других оценили данную запись
# Примечание 1. Имена в формируемой и возвращаемой функцией строке должны располагаться в своем исходном порядке.
#
# Примечание 2. Обратите внимание, что если в передаваемом в функцию списке более трех имен,
# то явно указываются лишь первые два из них.



def likes(names):
    if len(names) < 1:
        return 'Никто не оценил данную запись'
    elif len(names) == 1:
        return '{} оценил(а) данную запись'.format(*names)
    elif len(names) == 2:
        return '{} и {} оценили данную запись'.format(*names)
    elif len(names) == 3:
        return '{}, {} и {} оценили данную запись'.format(*names)
    else:
        return '{}, {} и {} других оценили данную запись'.format(*names[:2], (len(names) - 2))







print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))








