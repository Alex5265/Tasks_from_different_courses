# На вход программе подается строка с именем текстового файла.
# Напишите программу, которая выводит на экран его предпоследнюю строку.
# Формат входных данных
# На вход программе подается строка текста с именем существующего текстового файла.
# Формат выходных данных
# Программа должна вывести предпоследнюю строку указанного файла.
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Гарантируется, что файл содержит хотя бы две строки.
# Примечание 3. Не забудьте закрыть файл 🙂.


# принимаем название файла
file_name = input()

# создаем ссылку на файл - чтение текст, кодировка ютф(как рекомендуется )
file_point = open(file_name, 'rt', encoding='utf-8')
# в переменную считываем построчно все файлы с удалением лишних пробелов
prelast_line = list(map(str.strip, file_point.readlines()))

# закрываем файл
file_point.close()
# выводим на печать предпоследний файл
print(prelast_line[-2])




# languages_work_file_00