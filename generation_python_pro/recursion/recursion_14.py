# Реализуйте функцию range_sum() с использованием рекурсии,
# которая принимает три аргумента в следующем порядке:
#
# numbers — список целых чисел
# start — целое неотрицательное число
# end — целое неотрицательное число
# Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end]
# включительно и возвращать полученный результат.
#
# Примечание 1. Рассмотрим первый тест. Диапазону индексов [3;7]
# в переданном списке принадлежат числа 30
# 4+5+6+7+8=30
# Примечание 2. Гарантируется, что start <= end.
#
# Примечание 3. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию range_sum(), но не код, вызывающий ее.




def range_sum(numbers, start, end):
    if start >= end:
        return numbers[end]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)




print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))











