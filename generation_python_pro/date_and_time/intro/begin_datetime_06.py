# Вам доступен список dates, содержащий даты.
# Дополните приведенный ниже код, чтобы он вывел год и номер квартала каждой даты из данного списка.
# Компоненты дат должны быть расположены в исходном порядке, каждые на отдельной строке, в следующем формате:
# <год>-Q<номер квартала>
# Примечание 2. Начальная часть ответа выглядит так:
# 2010-Q3
# 2017-Q1


from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13),
         date(2009, 12, 25), date(2010, 2, 27),
         date(2021, 10, 11), date(2020, 3, 13),
         date(2000, 7, 7), date(1999, 4, 14),
         date(1789, 11, 19), date(2013, 8, 21),
         date(1666, 6, 6), date(1968, 5, 26)]



for d in dates:
    print(f'{d.year}-Q{(d.month + 2) // 3}')
