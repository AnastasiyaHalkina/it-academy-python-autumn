# Дан текст (строк может быть много, разделенных \n).
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то,
# которое меньше в лексикографическом порядке.

text = str(input('Enter words: '))
lst = text.replace('\\n', ' ').split()

lst1 = []
for el in lst:
    lst1.append(el.strip(" ,.!:?;"))

dct = {}
for element in lst1:
    dct[element] = dct.get(element, 0) + 1
lst2 = sorted(dct.values())
value_max = lst2[-1]

result = [key for key in dct if dct[key] == value_max]
result.sort()
print(result[0])
