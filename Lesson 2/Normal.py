# -*- coding: utf-8 -*-
__author__= 'Kozlov Aleksandr Anatiolevich'

import math
import datetime
import random

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

def create_list_with_input_number(length_list):
    """Создание списка из целых чисел с вводом из клавиатуры.
        Args:
            length_list: количество элементов списка.
        Returns:
            list: список чисел.
    """
    i = 0
    list = []
    print("Длина списка будет = ", length_list)
    while i < length_list:
        list.append(int(input("Введите {i} элемент списка: ".format(i=i))))
        i += 1
    return list

def check_sqrt_elements(list):
    """Проверка элементов списка на существования квадратного корня, в качестве целого числа.
        Args:
            list: список, элементы которого мы првоеряем
        Returns:
            sqrt_list: список со значениями квадратных корней, если они существуют.
    """
    result_list = []
    for element in list:
        if element < 1 or float(math.sqrt(element)) != int(math.sqrt(element)):
            continue
        result_list.append(int(math.sqrt(element)))
    return result_list

"""lentgh_list = int(input("Введите количество элементов списка: "))
list = create_list_with_input_number(lentgh_list)
print("Вы создали список: ", list)
result_list = check_sqrt_elements(list)
print("Список существующих целых квадратных корней: ", result_list)"""

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

def generate_random_list(length_list, min , max):
    """Получение списка со случайными числами.
        Args:
            length_list: длина списка.
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

"""length_list = int(input('Введите длину списка = '))
min = int(input('Введите нижнюю грацницу диапозона = '))
max = int(input('Введите верхнюю грацницу диапозона = '))
random_list = generate_random_list(length_list, min, max)
if random_list:
    print(random_list)
else:
    print("Вы ввели неверные данные!")"""

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

"""lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst1 = list(set(lst))
print(lst1)
lst2 = []
for element in lst:
    if lst.count(element) == 1:
        lst2.append(element)
print(lst2)"""

