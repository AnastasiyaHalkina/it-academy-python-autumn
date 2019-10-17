# Входные данные:
# Количество строк N. n = 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# Количество запросов M. m = 3
# Названия искомых М городов:
# Odessa
# Moscow
# Novgorod
# Выходные данные:
# Ukraine
# Russia
# Russia

n = int(input('Enter N: '))
dct = {}
for i in range(n):
    country, *cities = str(input('Enter country fnd cities: ')).split()
    for city in cities:
        dct.update({city: country})

m = int(input('Enter M: '))
lst = []
for j in range(m):
    cities_m = str(input('Enter city to search: '))
    lst.append(cities_m)

for city_m in lst:
    print(dct[city_m])
