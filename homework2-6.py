# Определите, является ли число палиндромом.  Число положительное целое, произвольной длинны.
number = str(input('Enter number: '))
if number[::] == number[::-1]:
    print('Yes!')
else:
    print('No')
