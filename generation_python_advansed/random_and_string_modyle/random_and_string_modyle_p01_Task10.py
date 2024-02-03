# Задачи на модуль рандом и стринг.
# Необходимо написать код, создаюущий карточку для бинго
# карточка 5х5 с уникальными числами от 1 до 75 при этом центральная клетка является пустой(заполняется числом 0)

from random import sample

n = 5
num = sample(list(range(1, 76)), 25)
num[(n * 2) + (n // 2)] = 0
num = [str(i).ljust(3) for i in num]

for i in range(0, len(num), n):
    print(*num[i:i + n])




