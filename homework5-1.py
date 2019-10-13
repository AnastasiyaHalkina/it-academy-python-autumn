""" Define a dict comprehension which returns a dictionary
where the keys are numbers between 1 and n (both included)
 and the values are square of keys. n – function argument.
 Default is 20."""


def dct_sqr(n=20):
    dct = {el: el ** 2 for el in range(1, n + 1)}
    return dct


print(dct_sqr())
