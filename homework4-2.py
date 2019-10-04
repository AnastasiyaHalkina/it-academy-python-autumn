import copy
# Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
lst = [chr(97 + i) + chr(98 + j) for i in range(2) for j in range(3)]
print(lst)
# Use a slice on the above list to construct the list ['ab', 'ad', 'bc']
lst1 = lst[::2]
print(lst1)
# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a']
lst = [str(el + 1) + 'a' for el in range(4)]
print(lst)
# Simultaneously remove the element '2a' from the above list and print it.
lst.remove('2a')
print(lst)
"""Copy the above list and add '2a' back into the list such 
that the original is still missing it."""
lst2 = copy.copy(lst)
lst2[1] = '2a'
lst2 = lst2[:2] + lst[1:]
print(lst2)
print(lst)
