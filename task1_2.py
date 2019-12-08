# Измените предложенную функцию, чтобы она использовала try-except
# который ловит возможный IndexError.
# Ошибка индексации может появиться если индекс больше длины списка.
# напечатайте сообщение если это произошло.


def print_list_element(thelist, index):
    try:
        print(thelist[index])
        return thelist[index]
    except IndexError as e:
        print("Error!", e)
