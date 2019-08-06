def calculate_num(num):
    digits = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    if num in digits:
        return digits[num]
    else:
        return num


number = input ('Phone number: ')

result = map(calculate_num, number)

print(list(result))
