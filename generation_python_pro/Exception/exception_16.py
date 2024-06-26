# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Реализуйте функцию is_good_password() в стиле LBYL,
# которая принимает один аргумент:
#
# string — произвольная строка
# Функция должна возвращать True, если строка string представляет собой хороший пароль,
# или False в противном случае.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую
# только необходимую функцию is_good_password(), но не код, вызывающий ее.


def is_good_password(string):
    return all([len(string) >= 9,
               any(str(s).isupper() for s in string),
               any(str(s).islower() for s in string),
               any(str(s).isdigit() for s in string)])



print(is_good_password('МойПарольСамыйЛучший111'))






