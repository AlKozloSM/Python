 # -*- coding: utf-8 -*-
__author__= 'Kozlov Aleksandr Anatiolevich'

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

"""new_list = [element ** 2 for element in list]
print(list)
print(new_list)"""

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

"""fruit_list1 = ["банан","апельсин","яблоко","ананас","абрикос","персик","гранат","груша"]
fruit_list2 = ["киви","дыня","арбуз","персик","банан","яблоко","ананас","персик","манго"]
result_list = [fruit for fruit in fruit_list1 if fruit in fruit_list2]
print result_list"""

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

"""numbers_list = [1,5,9,65,34,51,98,64,50,-6,-7]
result_list = [num for num in numbers_list if num % 3==0 and num % 4 != 0 and num > 0]
print(result_list)"""