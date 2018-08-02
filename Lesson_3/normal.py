# -*- coding: utf-8 -*-
__author__= 'Kozlov Aleksandr Anatiolevich'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """Функция, возвращающая ряд Фибоначчи с n по m элементы
    Args:
        n: первый элемент в списке чисел Фибоначчи.
        m: последний элемент в списке чисел Фибоначчи.
    Returns:
        fibonacci_list: список элементов с n по m.
    """
    if m < n:
        print("Неаправильно введены данные m не может быть меньше n")
    fibonacci_list = []
    fibonacci_elements = [1, 1]
    for i in range(1, m + 1):
        if n <= i:
            fibonacci_list.append(fibonacci_elements[1])
        if i == m:
            return fibonacci_list
        new_element = fibonacci_elements[0] + fibonacci_elements[1]
        fibonacci_elements[0] = fibonacci_elements[1]
        fibonacci_elements[1] = new_element

"""n = 5
m = 8
print(fibonacci(n, m))"""

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    i = 0
    n = 1
    max = origin_list[0]
    while i < len(origin_list):
         n = i + 1
         while n < len(origin_list):
             if origin_list[i] < origin_list[n]:
                max = origin_list[n]
                origin_list[n] = origin_list[i]
                origin_list[i] = max
             n += 1
         i += 1
    return origin_list

"print(sort_to_max([0,-19,14,13.2,90,0,-9,-0.7]))"

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_function(list, expression):
    result_list = []
    for i in list:
        if i == expression:
            result_list.append(i)
    return result_list
"""print(filter_function([1,3,2,4,56,234,256,7,23434,11,231], 3))"""

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def check_parallelogramm(a1, a2, a3, a4):
    length_1_side = (a3[0] - a4[0]) ** 2 + ((a3[1] - a4[1]) ** 2)
    length_2_side = (a2[0] - a1[0]) ** 2 + ((a2[1] - a1[1]) ** 2)
    length_3_side = (a4[0] - a1[0]) ** 2 + ((a4[1] - a1[1]) ** 2)
    length_4_side = (a3[0] - a2[0]) ** 2 + ((a3[1] - a2[1]) ** 2)
    if length_1_side == length_2_side and length_3_side == length_4_side:
        return True
    return False
"""a1=[2, 2]
a2=[4, 3]
a3=[5, 5]
a4=[3, 4]
print(check_parallelogramm(a1, a2, a3, a4))"""
