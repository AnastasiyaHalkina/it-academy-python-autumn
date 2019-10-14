# Вводится строка. Требуется удалить из нее
# повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def",
# то должно быть выведено "abcdef".

text = str(input('Enter text: '))
text1 = text.replace(' ', '')
result = ''
for symbol in text1:
    if symbol not in result:
        result += symbol
print(result)
