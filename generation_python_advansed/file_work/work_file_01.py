# На вход программе подается строка с именем текстового файла.
# Напишите программу, которая выводит на экран его содержимое.
# Формат входных данных
# На вход программе подается строка текста с именем существующего текстового файла.
# Формат выходных данных
# Программа должна вывести содержимое указанного файла.
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Не забудьте закрыть файл 🙂.



# получаем название файла
name_file = input()
# создаем ссылку на файл применяем функцию открыть с возможностью чтения(только)
# и названием переменной file
file = open(name_file, 'r')
# в переменную контент считываем построчно информацию из файла преобразуя информацию в строку
# убирая разделитель преобразуя в список
content = list(map(str.rstrip, file.readlines()))
# закрываем файл
file.close()

# выводим на печать
print(*content)