# -*- coding: utf-8 -*-
__author__ = 'Kozlov Aleksandr Anatiolevich'

import math

# Level: easy
# Урок 1.
# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

random_number = random.uniform(1, 100)
i = 0
extra_symbol = "."
while i < len(str(random_number)):
    if extra_symbol != random_number:
        print(str(random_number)[i])
    i += 1

random_number = random.uniform(1, 100)
extra_symbol = "."
for symbol in str(random_number):
    if not symbol == extra_symbol:
        print(symbol)
print(random_number)
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input('Введите первое число: ')
b = input('Введите второе число: ')
x = a
a = b
b = x
print('a= ', a)
print('b= ', b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = input('Введите ваш возраст: ')
if age < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")
