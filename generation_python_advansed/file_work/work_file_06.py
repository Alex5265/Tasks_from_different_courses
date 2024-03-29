# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:
# наименование товара;
# количество товара (целое число)
# цена (в рублях) товара за 1 шт (целое число).
# Напишите программу, выводящую на экран общую стоимость заказа.
# Формат входных данных
# На вход программе ничего не подается.
# Формат выходных данных
# Программа должна вывести общую стоимость заказа.
# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.



# чтобы не громоздить разбил на некоторые части
# сначала открываем файл для чтения текста
# в переменную линии считываем построчно и разбиваем сплитом
# в переменную товар записываем вычисления количества товара умноженное на цену товара
# в конце выводим общую сумму товара
with open('prices_work_06.txt', 'rt', encoding='utf-8') as file:
    lines = map(str.split, file.readlines())
    tovar = list(map(lambda line: int(line[1]) * int(line[2]), lines))
    print(sum(tovar))