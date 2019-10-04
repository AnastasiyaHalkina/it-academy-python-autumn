lst = [element + 1 for element in range(100)]
for el in lst:
    if el % 15 == 0:
        el = 'FizzBuzz'
    elif el % 3 == 0:
        el = 'Fizz'
    elif el % 5 == 0:
        el = 'Buzz'
    print(el)
