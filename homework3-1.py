# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания

a = str(input('Enter phrase: '))
lst = a.split()
n = len(lst)
lst_new = [lst[i].strip(' .,!?:;"') for i in range(n)]
max_word = lst_new[0]
for element in lst_new:
    if len(element) >= len(max_word):
        max_word = element
print(max_word)
