# Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор,
# бесконечно генерирующий единственное значение — строку i love beegeek!.
#
# Примечание. В тестирующую систему сдайте программу,
# содержащую только необходимый итератор infinite_love.


infinite_love = iter(lambda: 'i love beegeek!', -1)



print(next(infinite_love))
print(next(infinite_love))
print(next(infinite_love))














