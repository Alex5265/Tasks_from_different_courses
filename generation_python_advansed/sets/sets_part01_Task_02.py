# Тренировка работы с множествами.
# Необходимо написать программу для определения количества учеников :
# которые прочитали только одну книгу,
# прочитали две книги
# не прочитали ни одной рекомендованной книги
#
# если n прочитали первую книгу
# m прочитали вторую книгу
# k прочитали третью книгу
# x прочитали первую или вторую книгу, или обе книги
# прочитали вторую или третью, или обе книги
# z прочитали первую или третью, или обе книги
# t полностью прочитали все книги
# a всего учеников в классе

n, m, k, x, y, z, t, a = [int(input()) for i in 'nmkxyzta']

a_b = -1 * (x - n - m)
b_c = -1 * (y - m - k)
c_a = -1 * (z - n - k)

only_a_b = a_b - t
only_b_c = b_c - t
only_c_a = c_a - t

one_a = n - t - only_c_a - only_a_b
one_b = m - t - only_b_c - only_a_b
one_c = k - t - only_b_c - only_c_a

print(one_a + one_b + one_c)
print(only_a_b + only_b_c + only_c_a)
print(a - t - (one_a + one_b + one_c) - (only_a_b + only_b_c + only_c_a))


# 19
# 18
# 22
# 32
# 33
# 35
# 2
# 50
# На выходе
# 29
# 12
# 7
#


