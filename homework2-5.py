""" Задача взята с сайта https://py.checkio.org
Условие задачи: Дан массив с положительными числами и число N.
Вы должны найти N-ую степень элемента в массиве с индексом N.
 Если N за границами массива, тогда вернуть -1.
 Не забывайте, что первый элемент имеет индекс 0.
Входные значения: Два агумента. Массив как список целых и число как целое.
Выходные значения: Целое число.
"""


def index_power(array: list, n: int) -> int:
    # Find Nth power of the element with index N.

    if n < len(array):
        result = int(array[n]) ** n
    else:
        result = -1
    return result


array1 = list(input('Enter list: '))
n1 = int(input('Enter N: '))
print(index_power(array1, n1))
