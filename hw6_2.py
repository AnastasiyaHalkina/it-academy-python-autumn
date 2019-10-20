# Создайте декоратор, который хранит в файле результаты вызовы функций
# (за все время, не только текущий запуск программы)


def decor(func):
    def wrapper(x):
        result = func(x)
        f = open('results.txt', 'a')
        f.write('{}\n'.format(result))
        f.close()
    return wrapper


@decor
def func(x):
    return x + 1


func(3)
func(4)
func(10)
