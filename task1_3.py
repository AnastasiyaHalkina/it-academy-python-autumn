# Предложенная функция добавляет элемент в список
# внутри словаря списков. Перепишите ее, используя
# обработчик исключений так, чтобы он ловил возможный KeyError
# если список с именем не представлен в словаре,
# вместо использования проверки вхождения имени списка в словарь.
# Включите else-finally блок при необходимости.


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))
    return thedict
