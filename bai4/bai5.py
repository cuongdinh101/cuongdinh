str = "GreatPython"
islower = ''
isupper = ''

for i in range(len(str)):
    if str[i].islower():
        print(str[i], "là chữ thường")
        islower += str[i]
    elif str[i].isupper():
        print(str[i], "là chữ hoa")
        isupper += str[i]
    else:
        print(str[i], "không phải là chữ cái")

sorted_str = ''.join(sorted(islower) + sorted(isupper))
print('Kết quả:', sorted_str)
