# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума). Пример:
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint


def create_number(phrase):
    number = int(input(phrase))
    return number


def create_array(quan1, min1, max1):
    array2 = [randint(min1, max1) for i in range(quan1)]
    print(f"Создан массив элементов: {array2}")
    return array2


def find_list_of_indexes(arr2, min2, max2):
    arr3 = []
    for i, j in enumerate(arr2):
        if min2 <= j <= max2:
            arr3.append(i)
    print(f"Диапазону от {min2} до {max2} принадлежат индексы: {arr3}")


arr_quan = create_number("Введите колличество элементов массива: ")
arr_min = create_number("Введите минимальное значение элемента массива: ")
arr_max = create_number("Введите максимальное значение элемента массива: ")

num_min = create_number("Введите минимальное значение диапазона: ")
num_max = create_number("Введите максимальное значение диапазона: ")

array1 = create_array(arr_quan, arr_min, arr_max)

find_list_of_indexes(array1, num_min, num_max)
