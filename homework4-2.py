import copy

# Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
lst = [x + y for x in ['a', 'b'] for y in ['b', 'c', 'd']]
print('Task 1:', lst)

# Use a slice on the above list to construct the list ['ab', 'ad', 'bc']
lst1 = lst[::2]
print('Task 2:', lst1)

# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a']
lst = [str(el) + 'a' for el in range(1, 5)]
print('Task 3:', lst)

# Simultaneously remove the element '2a' from the above list and print it.
print('Task 4:', lst.pop(1))

""" Copy the above list and add '2a' back into the list such
that the original is still missing it."""
lst2 = copy.copy(lst)
lst2[1] = '2a'
lst2 = lst2[:2] + lst[1:]
print('Task 5:', 'lst2 =', lst2, 'lst = ', lst)
