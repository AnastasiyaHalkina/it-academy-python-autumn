# Реализовать функцию get_ranges которая получает на вход
# непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список "сворачивает"


def get_ranges(lst):
    result = ''
    for i in range(len(lst) - 1):
        if lst[i] + 1 == lst[i + 1] and lst[i] - 1 != lst[i - 1]:
            result += '{}-'.format(lst[i])
        elif lst[i] + 1 != lst[i + 1]:
            result += '{}, '.format(lst[i])
        elif lst[i] + 1 == lst[i + 1] and lst[i] - 1 == lst[i - 1]:
            result += ''
    result += str(lst[-1])
    print(result)


lst1 = list(map(int, input('Enter numbers separated by spaces: ').split()))
get_ranges(lst1)
