# Вам доступен текстовый файл lines.txt из нескольких строк.
# Напишите программу, которая выводит на экран случайную строку из этого файла.
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна вывести случайную строку указанного файла.
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Гарантируется, что файл содержит хотя бы одну строку.
# Примечание 3. Не забудьте закрыть файл .


# импортируем модуль рандом
import random

#создаем ссылку на файл задаем имя, только счетние текса, кодировку (есть слова на разых языках)
file_lines = open('lines_work_03.txt', 'rt', encoding='utf-8')
#в переменную сохраняем список значений построчно
content = list(map(str.strip, file_lines.readlines()))
# закрываем файл
file_lines.close()
# генерируем случайное число с помощью метода случайного int'a где А- 0 Б - длина списка - 1
random_line = random.randint(0, len(content) - 1)

# печатаем список [случайную линию]
print(content[random_line])

# lines_work_03.txt

#понравилось решение другого студента :

# у рандома есть еще метод вывода просто случайного элемента random.choice
# в данном случае действительно сокращает код и делает его компактнее
import random
content_01 = open('lines_work_03.txt', 'r', encoding='utf-8')
print(random.choice(content_01.readlines()))

content_01.close()



























# languages_work_file_00