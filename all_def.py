"""
Модуль с функциями, которые тестируются.
"""


def second_index(text, symbol):
    # returns the second index of a symbol in a given text

    if text.count(symbol) < 2:
        return None

    first_enter = text.find(symbol)
    result = text.find(symbol, first_enter + 1)
    return result


def first_word(text):
    # returns the  first word in a given text

    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]


def index_power(array, n):
    # Find Nth power of the element with index N.

    if n < len(array):
        result = int(array[n]) ** n
    else:
        result = -1
    return result


def get_long_word(text):

    """Найти самое длинное слово в введенном предложении.

    Учтите что в предложении есть знаки препинания
    """

    lst = text.split()
    n = len(lst)
    lst_new = [lst[i].strip(' .,!?:;"') for i in range(n)]
    max_word = lst_new[0]

    for element in lst_new:
        if len(element) >= len(max_word):
            max_word = element
    return max_word


def get_new_string(text):
    # Вводится строка. Требуется удалить из нее
    # повторяющиеся символы и все пробелы.

    text1 = text.replace(' ', '')

    result = ''
    for symbol in text1:
        if symbol not in result:
            result += symbol
    return result


def count_words(text):
    # Посчитать количество строчных (маленьких) и
    # прописных (больших) букв в введенной строке.
    # Учитывать только английские буквы.

    down_l = 0
    upper_l = 0

    for symbol in text:
        if 'a' <= symbol <= 'z':
            down_l += 1
        elif 'A' <= symbol <= 'Z':
            upper_l += 1
    return down_l, upper_l


def count_me_string(text):
    # Define a code which count
    # and return the numbers of each character
    # in a count_me_string argument.

    dct = {}
    for symbol in text:
        dct[symbol] = dct.get(symbol, 0) + 1
    return dct
