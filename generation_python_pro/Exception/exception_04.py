# Требовалось написать программу, которая принимает на вход два целых числа a и b,
# каждое на отдельной строке, и выводит список всех целых чисел от a до b включительно,
# которые делятся на 7 без остатка. Программист торопился и написал программу неправильно.
#
# Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 5).
#
# Примечание. Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.


a = int(input()) #1
b = int(input()) #2
numbers = []

for i in range(a, b+ 1): # 5
    if i % 7 == 0: # 4
        numbers.append(i) # 3

print(numbers)




