# Определите, является ли число палиндромом.
number = str(input('Enter number: '))
if number[::] == number[::-1]:
    print('Yes!')
else:
    print('No')
