# d = {'name':'harsh','profession':'Trainer', 'location':'London'}
# print(type(d))
# print(d['location'])
# print(len(d))
# d['name'] = 'Kenan'
# print(d)
# del d['name']
# print(d)


# def calc(a,b,c,d=4):
#     res = ((a+b+c)/(b+c)**(c/a))/d
#     return res

# x = calc(b=4, a=7, c=9)
# y = calc(7,4,9)
# z = calc(4,7,9,4)

# print(x, y ,z)

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')