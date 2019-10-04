a = str(input('Enter phrase: '))
down_l = 0
upper_l = 0
for symbol in a:
    if 'a' <= symbol <= 'z':
        down_l += 1
    elif 'A' <= symbol <= 'Z':
        upper_l += 1
    else:
        down_l = down_l
        upper_l = upper_l
print(down_l, upper_l)
