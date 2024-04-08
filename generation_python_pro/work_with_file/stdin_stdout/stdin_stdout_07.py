# Напишите программу, которая выводит все новости заданной категории,
# располагая их по возрастанию степени достоверности.
#
# Формат входных данных
# На вход программе подается произвольное количество строк, в каждой строке,
# кроме последней, записана новость, категория, к которой она относится,
# и ее достоверность в следующем формате:
#
# <новость> / <категория> / <достоверность>
# В последней строке подается одиночная категория.
#
# Формат выходных данных
# Программа должна вывести все новости, которые относятся к введенной категории.
# Новости должны быть расположены в порядке возрастания степени достоверности,
# а при совпадении степеней достоверности — в лексикографическом порядке самих новостей.
import sys

events, priory_tag = {}, None

for line in sys.stdin:
    line = line.strip().split(' / ')
    if len(line) > 1:
        event, tag, score = line
        events.setdefault(tag, []).append((score, event))
    else:
        priory_tag = line[0]

for _, event in sorted(events[priory_tag]):
    print(event)





