# Анаграммы — это слова, которые состоят из одинаковых букв. Например:
#
# адаптер — петарда
# адресочек — середочка
# азбука — базука
# аистенок — осетинка
# Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
#
# word — слово в нижнем регистре
# words — список слов в нижнем регистре
# Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.
#
# Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.
#
# Примечание 2. Считайте, что слово является анаграммой самого себя.

def filter_anagrams(word, words):
    word = sorted(word)
    result = []
    for i in words:
        if sorted(i) == word:
            result.append(i)
    return result




word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
# ['aabb', 'bbaa']
print()

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
# ['сеточка', 'стоечка', 'тесачок', 'чесотка']



