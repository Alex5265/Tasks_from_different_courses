# Напишите программу с использованием рекурсии,
# которая принимает на вход число и выводит количество цифр в этом числе.
#
# Формат входных данных
# На вход программе подается неотрицательное целое число.
#
# Формат выходных данных
# Программа должна определить количество цифр в введенном числе и вывести полученный результат.


def try_recursio_11(num):
    if num < 10:
        return 1
    else:
        return 1 + try_recursio_11(num // 10)


print(try_recursio_11(int(input())))



