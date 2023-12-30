# Тренировка вложенных списков.
# Задание (желательно написать функцию) подается строка и число, необходимо разбить на вложенные списки по числу

def chunked(symbols, n):
    # Пустой список
    result = []
    z = 0
    x = n
    # В цикле делается срез от 0 до n затем меняются параметры для дальнейшего среза
    # делается это до тех пор пока x не станет больше длины символом с прибавкой половины длины n т.к. цикл вайл сначала проверяет параметры
    while x <= (len(symbols) + (n // 2)):
        result.append(symbols[z:x])
        z = x
        x += n

    return result

#получаем символы
symbols = input().split()
#получаем необходимую длину среза
n = int(input())

print(chunked(symbols, n))
