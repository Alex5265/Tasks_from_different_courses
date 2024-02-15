# Напишите функцию info_kwargs(), которая принимает произвольное количество
# именованных аргументов и печатает именованные аргументы в соответствии с образцом:
# <имя аргумента>: <значение аргумента>, при этом имена аргументов следуют
# в алфавитном порядке (по возрастанию).


# благодоря синтаксису возможно получать именованые аргументы в виде словаря
# задание просто - получить и вывести в необходимом формате
def info_kwargs(**kwargs):
    for k,v in sorted(kwargs.items()):
        print(f"{k}: {v}")


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')