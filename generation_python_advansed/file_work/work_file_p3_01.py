# Напишите программу, которая считывает строку текста и записывает её
# в текстовый файл output.txt.
# Формат входных данных
# На вход программе подается строка текста.
# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него считанную строку текста.
# Примечание. Считайте, что исполняемая программа и указанный файл находятся в одной папке.



# открываем(создаем) файлв режиме записи и с помощью принта и запроса Input записываем в него данные
with open('output_p3_01.txt', 'wt', encoding='utf-8') as output:
    print(input(), file=output)