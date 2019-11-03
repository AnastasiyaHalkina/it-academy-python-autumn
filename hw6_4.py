"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data6/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла
top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""

try:
    my_file = open('ratings.list', 'r', encoding="ISO-8859-1")
    for line in my_file:
        print(line)
    my_file.close()
except FileNotFoundError:
    print("File not found!")
