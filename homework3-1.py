a = str(input('Enter phrase: '))
lst = a.split()
n = len(lst)
lst_new = [lst[i].strip(' .,!?') for i in range(n)]
max_word = lst_new[0]
for i in range(n):
    if max_word <= lst_new[i]:
        max_word = lst_new[i]
print(max_word)
