# Даны два списка чисел. Посчитайте, сколько чисел
# входит только в один из этих списков.

lst1 = input('Enter the first list of numbers: ')
lst2 = input('Enter the second list of numbers: ')

lst3 = set(lst1) ^ set(lst2)
result = len(lst3)
print(result)
