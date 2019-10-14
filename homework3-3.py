# Посчитать количество строчных (маленьких) и
# прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

text = str(input('Enter phrase: '))
down_l = 0
upper_l = 0
for symbol in text:
    if 'a' <= symbol <= 'z':
        down_l += 1
    elif 'A' <= symbol <= 'Z':
        upper_l += 1
print(down_l, upper_l)
