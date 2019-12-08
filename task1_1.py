# Напишите функцию которая делит 5/0 и использует try - except
# который ловит исключение деления на ноль.


def divided_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError as e:
        print("Error!", e)
    else:
        return result
