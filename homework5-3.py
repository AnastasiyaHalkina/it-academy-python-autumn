# n = 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# m = 3
# city1 = Odessa
# city2 = Moscow
# city3 = Novgorod

n = int(input('Enter N: '))
dct = {}
for i in range(n):
    text = str(input('Enter country and cities: '))
    pos = text.find(' ')
    country = text[:pos]
    cities = text[pos + 1:].split()
    for city in cities:
        dct.update({city: country})
m = int(input('Enter M: '))
lst = []
for j in range(m):
    cities_m = str(input('Enter city to search: '))
    lst.append(cities_m)
for city_m in lst:
    print(dct[city_m])
