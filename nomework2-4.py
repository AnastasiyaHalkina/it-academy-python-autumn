""" Задача взята с сайта https://py.checkio.org
Условие задачи: Вам дана строка и два маркера (начальный и конечный).
Вам необходимо найти текст, заключенный между двумя этими маркерами.
Но есть несколько важных условий:
Начальный и конечный маркеры всегда разные
Если нет начального маркера, то началом считать начало строки
Если нет конечного маркера, то концом считать конец строки
Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
Input: Три аргумента. Все строки.
Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    # returns substring between two given markers

    pos = text.find(begin)
    num_start = pos + len(begin) if pos else 0
    pos = text.find(end)
    num_end = pos if pos else len(text)
    return text[num_start:num_end]


text1 = str(input('Enter text: '))
begin1 = str(input('Enter begin: '))
end1 = str(input('Enter end: '))
print(between_markers(text1, begin1, end1))
