# Даны два списка чисел. Посчитайте, сколько чисел
# входит только в один из этих списков.

lst1 = list(input('Enter the first list of numbers: '))
lst2 = list(input('Enter the second list of numbers: '))

a = set(lst1)
b = set(lst2)
lst3 = a - b
lst4 = b - a
result = len(lst3) + len(lst4)
print(result)
