# Тренировка работы с кортежами.
# Задание - необходимо дополнить код, так, чтобы получить список из не пустых кортежей не меняя порядок


tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if i]

print(non_empty_tuples)