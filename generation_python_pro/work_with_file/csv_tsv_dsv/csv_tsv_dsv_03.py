# Наступил ноябрь, и во многих магазинах начались распродажи,
# но как многим известно, зачастую товары со скидкой оказываются дороже,
# чем без нее. Вам доступен файл sales.csv, который содержит
# данные о ценообразовании различной бытовой техники.
# В первом столбце записано название товара, во втором — старая цена,
# в третьем — новая цена со скидкой:
#
# name;old_price;new_price
# Встраиваемая посудомоечная машина De'Longhi DDW 06S;23089;31862
# Вытяжка Falmec Afrodite 60/600;27694;18001
# ...
# Напишите программу, которая выводит названия тех товаров,
# цена на которые уменьшилась. Товары должны быть расположены в своем исходном порядке,
# каждый на отдельной строке.
#
# Примечание 1. Разделителем в файле sales.csv является точка с запятой,
# при этом кавычки не используются.
import csv

with open('sales.csv', 'r', encoding='UTF-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    real_sales = filter(lambda i: int(i['old_price']) > int(i['new_price']), rows)

    for row in real_sales:
        print(row['name'])








