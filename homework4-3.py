# Create the list ['a', 'b', 'c'], then create a tuple from that list
lst = [x for x in 'abc']
t = tuple(lst)
print('Task 1:', lst, t)

# Create the tuple ('a', 'b', 'c'),
# then create a list from that tuple.
# (Hint: the material needed to do this has been covered,
# but it's not entirely obvious)
t1 = ()
for x in 'abc':
    t1 += (x, )
lst = list(t1)
print('Task 2:', t, lst)

# Make the following instantiations simultaneously:
# a = 'a', b=2, c='gamma'. (That is, in one line of code).
a, b, c = 'a', 2, 'gamma'
print('Task 3:', a, b, c)

# Create a tuple containing just a single element
# which in turn contains the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.
lst = [x for x in 'abc']
t2 = (lst, )
n = len(t2)
print('Task 4:', t2, 'len(t2) = ', n)
