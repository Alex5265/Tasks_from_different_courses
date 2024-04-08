# Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт,
# а также магазин, в котором он продается. Вам доступен файл prices.csv,
# который содержит информацию о ценах продуктов в различных магазинах.
# В первом столбце записано название магазина, а в последующих — цена на соответствующий
# товар в этом магазине:
#
# Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;Вареники;Картофель;Батончик
# Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
# Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
# ...
# Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина,
# в котором он продается, в следующем формате:
#
# <название продукта>: <название магазина>
# Если имеется несколько самых дешевых товаров, то следует вывести тот товар,
# ье название меньше в лексикографическом сравнении. Если один товар продается в
# нескольких магазинах по одной минимальной цене, то следует вывести тот магазин,
# чье название меньше в лексикографическом сравнении.
#
# Примечание 1. Разделителем в файле prices.csv является точка с запятой,
# при этом кавычки не используются.
import csv


with open('prices.csv', encoding='UTF-8') as file:
    column, *data = csv.reader(file, delimiter=';')

    price = [(d[0],column[i], d[i])for d in data for i in range(1, len(column))]
    result = min(price, key=lambda x: (int(x[2]), x[1], x[0]))

    print(f'{result[1]}: {result[0]}')














