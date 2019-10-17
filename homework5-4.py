# Даны два списка чисел. Посчитайте, сколько чисел
# содержится одновременно как в первом списке, так и во втором.

lst1 = list(input('Enter the first list of numbers: '))
lst2 = list(input('Enter the second list of numbers: '))
lst3 = set(lst1) & set(lst2)
result = len(lst3)
print(result)
