# Реализуйте класс CardDeck, порождающий итераторы,
# конструктор которого не принимает никаких аргументов.
#
# Итератор класса CardDeck должен генерировать последовательность из
# 52
# 52 игральных карт, а после возбуждать исключение StopIteration.
# Каждая карта должна представлять собой строку в следующем формате:
#
# <номинал> <масть>
# Например, 7 пик, валет треф, дама бубен, король червей, туз пик.
#
# Примечание 1. Карты, генерируемые итератором, должны
# располагаться сначала по величине номинала, затем масти.
#
# Примечание 2. Старшинство мастей по возрастанию: пики, трефы, бубны, червы.
# Старшинство карт в масти по возрастанию: двойка, тройка, четверка, пятерка,
# шестерка, семерка, восьмерка, девятка, десятка, валет, дама, король, туз.
#
# Примечание 3. Масти не требуют склонения и независимо от номинала должны
# сохранять следующее написание: пик, треф, бубен, червей.
#
# Примечание 4. В тестирующую систему сдайте программу, содержащую только
# необходимый класс CardDeck.

class CardDeck:
    def __init__(self):
        self.cards = iter(f'{j} {i}' for i in ("пик", "треф", "бубен", "червей") for j in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"))


    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cards)



cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])












