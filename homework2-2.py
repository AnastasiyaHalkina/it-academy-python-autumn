"""Задача взята с сайта https://py.checkio.org/
Условие задачи: Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
Input: Две строки (String).
Output: Int or None
"""


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    if text.count(symbol) < 2:
        return None
    first_enter = text.find(symbol)
    result = text.find(symbol, first_enter + 1)
    return result
