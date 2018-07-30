# -*- coding: utf-8 -*-
__author__= 'Kozlov Aleksandr Anatiolevich'

import math

#Level: normal
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.

number = input('Введите целое беззнаковое число: ')
i = 0
max = 0
while i < len(str(number)):
    if max < int(str(number)[i]):
        max = int(str(number)[i])
    if max == 9:
        break
    i += 1
print('Максимальная цифра= ', max)

number = input('Введите целое беззнаковое число: ')
max = 0
for digit in str(number):
    if max < int(digit):
        max = int(digit)
    if max == 9:
        break
print('Максимальная цифра= ', max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.

a = input('Введите первое число: ')
b = input('Введите второе число: ')
a = a + b
b = a - b
a = a - b
print("a= ", a)
print("b= ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

def calculation_of_quadratic_equation(a, b, c):
    disc = b ** 2 - (4 * a * c)
    if a == 0:
        print("Уравнениее не является квадратным")
        return None
    if disc < 0:
        print("Уравнение не имеет решения")
        return None
    elif disc == 0:
        x = -b / (2 * a)
        print("Уравнение имеет 1 корень")
        return x
    else:
        x = (-b + math.sqrt(disc)) / (2 * a)
        y = (-b - math.sqrt(disc)) / (2 * a)
    return x, y

a = input("Введите коэффициент а:")
b = input("Введите коэффициент b:")
c = input("Введите коэффициент c:")
roots = calculation_of_quadratic_equation(a, b ,c)
print("Корни квадратного уравнения=", roots)
