# Create the list ['a', 'b', 'c'], then create a tuple from that list
lst = [chr(97 + i) for i in range(3)]
print(lst)
t = tuple(lst)
print(t)
# Create the tuple ('a', 'b', 'c'),
# then create a list from that tuple.
# (Hint: the material needed to do this has been covered,
# but it's not entirely obvious)
t1 = ()
for i in range(3):
    t1 += (chr(97 + i), )
print(t1)
lst = list(t1)
print(lst)
# Make the following instantiations simultaneously:
# a = 'a', b=2, c='gamma'. (That is, in one line of code).
a, b, c = 'a', 2, 'gamma'
print(a, b, c)
# Create a tuple containing just a single element
# which in turn contains the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.
lst = [chr(97 + i) for i in range(3)]
t2 = (lst, )
n = len(t2)
print(t2)
print(n)
