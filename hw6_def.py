def total_price(euro_one=1, cent_one=3, quantity=3):
    """Напишите программу, которая считает общую цену.
    Вводится M рублей и N копеек цена, а также количество L товара
    Посчитайте общую цену в рублях и копейках за L товаров."""

    c = cent_one / 100
    euro = int(euro_one * quantity + ((cent_one * quantity) // 100))
    res = (euro_one + c) * quantity
    cents = round((res - euro) * 100)
    return print('Total: {euro} euro {cents} cents'.format(euro=euro, cents=cents))


def second_index(text='abcdcef', symbol='c'):
    # returns the second index of a symbol in a given text

    if text.count(symbol) < 2:
        return None
    first_enter = text.find(symbol)
    result = text.find(symbol, first_enter + 1)
    return result


def first_word(text=' returns the  first word in a given text'):
    # returns the  first word in a given text

    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]


def between_markers(text='returns substring between two given markers', begin='two', end='markers'):
    # returns substring between two given markers

    pos = text.find(begin)
    num_start = pos + len(begin) if pos else 0
    pos = text.find(end)
    num_end = pos if pos else len(text)
    return text[num_start:num_end]


"""def index_power(array, n):
    # Find Nth power of the element with index N.

    if n < len(array):
        result = int(array[n]) ** n
    else:
        result = -1
    return result
"""

def get_long_word(text='Aaaa bbb ccccc d?'):
    """ Найти самое длинное слово в введенном предложении.
    Учтите что в предложении есть знаки препинания"""

    lst = text.split()
    n = len(lst)
    lst_new = [lst[i].strip(' .,!?:;"') for i in range(n)]
    max_word = lst_new[0]
    for element in lst_new:
        if len(element) >= len(max_word):
            max_word = element
    return max_word


def get_new_string(text='abc cde def'):
    """ Вводится строка. Требуется удалить из нее
    повторяющиеся символы и все пробелы."""

    text1 = text.replace(' ', '')
    result = ''
    for symbol in text1:
        if symbol not in result:
            result += symbol
    return result


def count_words(text='QqWwEeRrTtY!'):
    """ Посчитать количество строчных (маленьких) и
    прописных (больших) букв в введенной строке.
    Учитывать только английские буквы."""

    down_l = 0
    upper_l = 0
    for symbol in text:
        if 'a' <= symbol <= 'z':
            down_l += 1
        elif 'A' <= symbol <= 'Z':
            upper_l += 1
    return down_l, upper_l


def gen_numbers():
    """ Write a program that prints the numbers from 1 to 100,
    but for multiples of three print “Fizz” instead of the number
    and for multiples of five print “Buzz”.
    For numbers which are multiples of both three and five, print “FizzBuzz”."""

    lst = [element + 1 for element in range(100)]
    for el in lst:
        if el % 15 == 0:
            el = 'FizzBuzz'
        elif el % 3 == 0:
            el = 'Fizz'
        elif el % 5 == 0:
            el = 'Buzz'
        print(el)


def dct_sqr(n=20):
    """ Define a dict comprehension which returns a dictionary
    where the keys are numbers between 1 and n (both included)
     and the values are square of keys. n – function argument.
     Default is 20."""

    dct = {el: el ** 2 for el in range(1, n + 1)}
    return print(dct)


def count_me_string(text='aaabbc'):
    """ Define a code which count
    and return the numbers of each character in a count_me_string argument."""

    dct = {}
    for symbol in text:
        dct[symbol] = dct.get(symbol, 0) + 1
    return dct
