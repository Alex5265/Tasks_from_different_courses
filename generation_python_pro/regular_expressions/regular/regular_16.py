# HTML-элементы — основа языка HTML.
# Каждый HTML-элемент обозначается начальным (открывающим) и
# конечным (закрывающим) тегами. Открывающий и закрывающий теги
# содержат имя элемента. Открывающий тег может содержать дополнительную
# информацию — атрибуты и значения атрибутов:
#
# <b>BeeGeek</b>
# <a href="https://stepik.org">Stepik</a>
# В примере выше тег <b> не содержит никаких атрибутов,
# а тег <a> содержит атрибут href со значением https://stepik.org.
#
# Напишите программу, которая находит во фрагменте
# HTML-страницы все атрибуты каждого тега.
#
# Формат входных данных
# На вход программе подается произвольное количество
# строк, которые образуют фрагмент HTML-страницы.
#
# Формат выходных данных
# Программа должна найти в введенном фрагменте HTML-страницы
# все теги и вывести их, указав для каждого соответствующие атрибуты.
# Теги вместе со всеми атрибутами должны быть расположены каждый на
# отдельной строке, в следующем формате:
#
# <тег>: <атрибут>, <атрибут>, ...
# Теги, а также атрибуты тегов, должны быть расположены в лексикографическом порядке.
#
# Примечание 1. Тестовые данные доступны по ссылкам:


#сторонее решение
import re

res = {}
for line in open(0):
    for tag, params in re.findall(r'<(\w+)(.*?)>', line):
        res.setdefault(tag, set()).update(re.findall(r'([\w-]+)=', params))

for key in sorted(res):
    print(f'{key}: {", ".join(sorted(res[key]))}')































