# Реализуйте функцию is_palindrome() с использованием рекурсии,
# которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать значение True,
# если переданная строка является палиндромом, или False в противном случае.
#
# Примечание 1. Палиндром — текст, одинаково читающийся в обоих направлениях.
#
# Примечание 2. Пустая строка является палиндромом, как и строка,
# состоящая из одного символа.
#
# Примечание 3. В тестирующую систему сдайте программу,
# содержащую только необходимую функцию is_palindrome(), но не код, вызывающий ее.


def is_palindrome(string):
    if len(string) in [1, 0]:
        return True
    elif string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])





print(is_palindrome('122333221'))





