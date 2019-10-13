# Define a code which count
# and return the numbers of each character in a count_me_string argument.


def count_me_string(text):
    dct = {}
    for symbol in text:
        dct[symbol] = dct.get(symbol, 0) + 1
    return dct


text1 = str(input('Enter the string: '))
print(count_me_string(text1))
