text = "abc cde def"
lst = text.replace(' ', '').split()
print(lst)
result = []
for el in lst:
    if lst.count(el) == 1:
        result.append(el)
print(result)
