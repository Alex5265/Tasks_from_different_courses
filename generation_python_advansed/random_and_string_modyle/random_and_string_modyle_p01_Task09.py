# Задачи на модуль рандом и стринг.
# Необходимо написать код, создает из принятого слова анаграмму
# т.е. в случайно порядке перемешивает буквы

import random

word = list(input())
random.shuffle(word)
print(''.join(word))
