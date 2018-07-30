# -*- coding: utf-8 -*-
__author__= 'Kozlov Aleksandr Anatiolevich'

import random

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

fruits_list = ["яблоко", "банан", "киви", "арбуз"]
number = 0
for fruit in fruits_list:
    number += 1
    print('{number} {fruit:>10}'.format(number=number, fruit=fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

first_list = [1,2,3,4,5,6]
second_list = [3,4,6,8,9]
result_list = list(set(first_list)-set(second_list))
print(result_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

def generate_random_list(length_list, min , max):
    """Получение списка со случайными числами.
        Args:
            length_list: длина списка
            min: нижняя граница диапозона чисел.
            max: верхняя граница диапозона чисел.
        Returns:
            list: список со случайными числами.
    """
    if max < min:
        print("Верхняя граница меньше нижней границы")
        return None
    i = 0
    list = []
    while i < length_list:
        list.append(random.randint(min, max))
        i += 1
    return list

def check_multiplicity_list_elements(list):
    """Проверка кратности 2 элементов списка.
        Args:
            list: список, в котором проверяется кратность.
        Returns:
            multiplicity_list: изменнный список элементов.
    """
    multiplicity_list = []
    for element in list:
        if element % 2 == 0:
            multiplicity_list.append(element / 4)
        else:
            multiplicity_list.append(element * 2)
    return multiplicity_list

length_list = int(input('Введите длину списка = '))
min = int(input('Введите нижнюю грацницу диапозона = '))
max = int(input('Введите верхнюю грацницу диапозона = '))

list = generate_random_list(length_list, min, max)
if list:
    print('Начальный список : ', list)
    multiplicity_list = check_multiplicity_list_elements(list)
    print('Проверенный список : ', multiplicity_list)
else:
    print("Вы ввели неверные данные")



