# Оформите решение задач из прошлых домашних работ в функции.
# Напишите функцию runner.
# runner() – все фукнции вызываются по очереди
# runner(‘gen_numbers’) – вызывается только функцию gen_numbers.
# runner(‘func’, ‘func1’...) - вызывает все переданные функции

import hw6_def


def runner(*lst):
    lst_def = [attr for attr in dir(hw6_def) if 'a' <= attr[0] <= 'z']

    if len(lst) >= 1:
        for element in lst:
            func = getattr(hw6_def, element)
            print(func())
    else:
        for element_def in lst_def:
            func = getattr(hw6_def, element_def)
            print(func())


runner()
