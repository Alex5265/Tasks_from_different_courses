# Реализуйте функцию print_digits() с использованием рекурсии,
# которая принимает один аргумент:
#
# number — натуральное число
# Функция должна выводить все цифры числа number,
# начиная с младших разрядов, каждое на отдельной строке.
#
# Примечание 1. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию print_digits(), но не код, вызывающий ее.


def print_digits(number):
    if number:
        print(number % 10)
        print_digits(number // 10)







print_digits(12345)
