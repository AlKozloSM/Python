# -*- coding: utf-8 -*-
__author__= 'Kozlov Aleksandr Anatiolevich'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    """Функция округление числа
    Args:
        number: десятичное число.
        ndigits: количество цифр после запятой, которые нужно оставить.

    Return:
        Конечное округленное число.
    """
    if type(number) != float:
        print("Number не является типом float")
        return
    if type(ndigits) != int:
        print('Ndigits не является типом int.')
        return None
    number_list = str(number).split('.')
    if ndigits >= len(number_list[1]):
        return number
    elif ndigits == 0:
        if int((number_list[1])[0]) >= 5:
            return int(number_list[0]) + 1
        return int(number_list[0])
    elif ndigits < 0:
        print('Количество знаков не может быть отрицательным!')
        return None
    if int((number_list[1])[ndigits]) >= 5:
        number_list[1] = int((number_list[1])[:ndigits]) + 1
        return int(number_list[0]) + int(number_list[1]) / (10 ** ndigits)

a = 1455.34845
b = 10
c = my_round(a, b)
print(c)


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket):
    if type(ticket) != int:
        return None
    if len(str(ticket)) != 6:
        return None
    ticket_list = str(ticket / 1000).split('.')
    sum = 0
    for i in ticket_list:
        for digit in ticket_list[0]:
            if i == ticket_list[0]:
                sum += int(digit)
            else:
                sum -= int(digit)
    if sum != 0:
        return False
    return True


a = 569956
print(lucky_ticket(a))