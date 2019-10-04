# Задача № 1
m = int(input('Enter euro: '))
n = int(input('Enter cents: '))
q = int(input('Enter quantity of goods: '))
c = n / 100
euro = int(m * q + ((n * q) // 100))
res = (m + c) * q
cents = round((res - euro)*100)
print('Total: {euro} euro {cents} cents'.format(euro=euro, cents=cents))
