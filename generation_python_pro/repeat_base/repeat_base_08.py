# Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
#
# numbers — список целых чисел
# number — целое число
# Функция должна находить в списке numbers ближайшее по значению число к числу number
# и возвращать его индекс. Если список numbers пуст, функция должна вернуть число −1.
#
# Примечание 1. Если в функцию передается список, содержащий несколько чисел,
# одновременно являющихся ближайшими к искомому числу,
# функция должна возвращать наименьший из индексов ближайших чисел.
#



def index_of_nearest(numbers, number):
    # если длина списка меньше 1 возвращает -1
    if len(numbers) < 1:
        return -1
    # вычисляем минимальное значение для этого в ламда функции из значений списка вычитаем искомое необходимое
    # значение пример на 3 тесте будет показателен
    # список [9, 5, 3, 2, 11] вычитаем из каждого значение 4
    # получаем [5, 1, -1, -2, 7] получается что-то вроде списка в котором значения сообщают насколько
    # они близко к искомому единственное необходимо взять модуль чисел получаем [5, 1, 1, 2, 7]
    # т.е. получается что ближе всего к числу 4 значения - 5 и 3.
    min_val = min(numbers, key=lambda a: abs(a - number))
    return numbers.index(min_val)




print(index_of_nearest([], 17)) #-1
print(index_of_nearest([7, 13, 3, 5, 18], 0)) #2
print(index_of_nearest([9, 5, 3, 2, 11], 4)) #1
print(index_of_nearest([7, 5, 4, 4, 3], 4)) #2
print(index_of_nearest([6, 100, 101, 2], 4)) #0
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0)) #3
print(index_of_nearest([1, 14, 100, 65, 6], 5)) #4
print(index_of_nearest([10, 164, 100, 265, 16], 8)) #0
print(index_of_nearest([10, 99, 0, -12, 16], -9)) #3
print(index_of_nearest([1, 1, 1, 1, 1], 1)) #0
