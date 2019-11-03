"""
Модуль с функциями, которые используются для работы функции runner.
"""


def total_price():

    """Напишите программу, которая считает общую цену.
    Вводится M рублей и N копеек цена, а также количество L товара
    Посчитайте общую цену в рублях и копейках за L товаров.
    """

    euro_one = int(input('Enter euro for 1p.: '))
    cent_one = int(input('Enter cents for 1p.: '))
    quantity = int(input('Enter quantity of goods: '))

    c = cent_one / 100
    euro = int(euro_one * quantity + ((cent_one * quantity) // 100))
    res = (euro_one + c) * quantity
    cents = round((res - euro) * 100)
    return 'Total: {euro} euro {cents} cents'.format(euro=euro, cents=cents)


def second_index():
    # returns the second index of a symbol in a given text

    text = str(input('Enter text: '))
    symbol = str(input('Enter symbol: '))

    if text.count(symbol) < 2:
        return None

    first_enter = text.find(symbol)
    result = text.find(symbol, first_enter + 1)
    return result


def first_word():
    # returns the  first word in a given text

    text = str(input('Enter text: '))

    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]


def between_markers():
    # returns substring between two given markers

    text = str(input('Enter text: '))
    begin = str(input('Enter begin marker: '))
    end = str(input('Enter end marker: '))

    pos = text.find(begin)
    num_start = pos + len(begin) if pos else 0
    pos = text.find(end)
    num_end = pos if pos else len(text)
    return text[num_start:num_end]


def index_power():
    # Find Nth power of the element with index N.

    array = list(input('Enter list of numbers: '))
    n = int(input('Enter index N: '))

    if n < len(array):
        result = int(array[n]) ** n
    else:
        result = -1
    return result


def get_long_word():

    """Найти самое длинное слово в введенном предложении.
    Учтите что в предложении есть знаки препинания
    """

    text = str(input('Enter text: '))

    lst = text.split()
    n = len(lst)
    lst_new = [lst[i].strip(' .,!?:;"') for i in range(n)]
    max_word = lst_new[0]

    for element in lst_new:
        if len(element) >= len(max_word):
            max_word = element
    return max_word


def get_new_string():

    """Вводится строка. Требуется удалить из нее
    повторяющиеся символы и все пробелы.
    """

    text = str(input('Enter text: '))

    text1 = text.replace(' ', '')

    result = ''
    for symbol in text1:
        if symbol not in result:
            result += symbol
    return result


def count_words():

    """Посчитать количество строчных (маленьких) и
    прописных (больших) букв в введенной строке.
    Учитывать только английские буквы.
    """

    text = str(input('Enter text: '))

    down_l = 0
    upper_l = 0

    for symbol in text:
        if 'a' <= symbol <= 'z':
            down_l += 1
        elif 'A' <= symbol <= 'Z':
            upper_l += 1
    return down_l, upper_l


def gen_numbers():

    """Write a program that prints the numbers from 1 to 100,
    but for multiples of three print “Fizz” instead of the number
    and for multiples of five print “Buzz”.
    For numbers which are multiples of both three and five,
    print “FizzBuzz”.
    """

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

    """Define a dict comprehension which returns a dictionary
    where the keys are numbers between 1 and n (both included)
     and the values are square of keys. n – function argument.
     Default is 20.
     """

    dct = {el: el ** 2 for el in range(1, n + 1)}
    return dct


def count_me_string():

    """Define a code which count
    and return the numbers of each character in a count_me_string argument.
    """

    text = str(input('Enter text: '))

    dct = {}
    for symbol in text:
        dct[symbol] = dct.get(symbol, 0) + 1
    return dct
