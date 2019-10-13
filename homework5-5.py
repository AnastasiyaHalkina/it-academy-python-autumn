lst1 = str(input('Enter the first list of numbers separated by spaces: '))
lst2 = str(input('Enter the second list of numbers separated by spaces: '))
a = set(lst1.split())
b = set(lst2.split())
lst3 = a - b
lst4 = b - a
result = len(lst3) + len(lst4)
print(result)
