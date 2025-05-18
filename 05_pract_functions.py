
'''Создайте функцию is_even, которая принимает одно число в
качестве параметра и возвращает True, если число чётное,
и False, если нечётное.'''
def is_even(num):
    return num %2 == 0
print(is_even(12))
print(is_even(3))

'''Задание 2: Умножение строки
Напишите функцию repeat_string, которая принимает два параметра:'''
def repeat_string(student,count):
    return student*count
result=repeat_string('Nurzaada ',3)
print(result)


'''Задание 3: Максимальное число
Создайте функцию find_max, которая принимает три числа и возвращает максимальное из них.
'''
def max_find(*numbers):
    return max(numbers)
max_num=max_find(2,15,25)
print(max_num)