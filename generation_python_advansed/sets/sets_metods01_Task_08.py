# Методы множеств
# Необходимо написать код на вход поступает число н
# затем н строк различных чисел. Необходим код который выводит все общие цифры в порядке возрастания

print(*sorted(set.intersection(*(set(input()) for i in range(int(input()))))))