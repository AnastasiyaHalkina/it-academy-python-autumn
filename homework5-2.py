text = str(input('Enter words: '))
lst = text.replace('\n', '').split()
dct = {}
for element in lst:
    dct[element] = dct.get(element, 0) + 1
lst1 = sorted(dct.values())
value_max = lst1[-1]
result = [key for key in dct if dct[key] == value_max]
result.sort()
print(result)
