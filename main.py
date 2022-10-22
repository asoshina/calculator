# Створіть інженерний калькулятор з використанням модуля math, в якому передбачене меню.
# Під час створення дотримуйтесь правил специфікації PEP 8.

def add(a, b):
    global expression
    if expression == '':
        expression = f'{a} + {b} '
    else:
        expression += f'+ {b} '
    return a + b


def myltiple(a, b):
    global expression
    if expression == '':
        expression = f'{a} * {b} '
    else:
        expression = f'({expression}) * {b}'
    return a * b


def degree(a, b):
    global expression
    if expression == '':
        expression = f'{a} ** {b} '
    else:
        expression = f'({expression}) ** {b}'
    return a ** b


def sub(a, b):
    global expression
    if expression == '':
        expression = f'{a} - {b} '
    else:
        expression = f'{expression} - {b}'
    return a - b


def division(a, b):
    if b != 0:
        global expression
        if expression == '':
            expression = f'{a} / {b} '
        else:
            expression = f'({expression}) / {b}'
        return a / b
    else:
        expression = ''
        print('division by zero')


def square(a):
    global expression
    if expression == '':
        expression = f'{a} ** 0.5 '
    else:
        expression = f'({expression}) ** 0.5'
    return a ** 0.5


def cube(a):
    global expression
    if expression == '':
        expression = f'{a} ** 1/3 '
    else:
        expression = f'({expression}) ** 1/3'
    return a ** (1 / 3)


def input1():
    a = int(input('a = '))
    return a


def input2():
    a = int(input('a = '))
    b = int(input('b = '))
    return a, b


expression = ''
result = 0
while True:
    i = int(input('\nchoose your action:\n1)сложение\t2)вычитание\t3)умножение\t4)деление\n5)возведение в степень\t6)'
                  'корень квадратный\t7)корень кубический\n11)exit\n12)clear\n>'))
    if expression == '':
        if 1 <= i <= 4:
            x, y = input2()
        elif 5 <= i <= 7:
            y = input1()
        match i:
            case 1:
                result = add(x, y)
                print(expression, '= ', result)
            case 2:
                result = sub(x, y)
                print(expression, '= ', result)
            case 3:
                result = myltiple(x, y)
                print(expression, '= ', result)
            case 4:
                result = division(x, y)
                if y != 0:
                    print(expression, '= ', result)
            case 5:
                result = degree(x, y)
                print(expression, '= ', result)
            case 6:
                result = square(y)
                print(expression, '= ', result)
            case 7:
                result = cube(y)
                print(expression, '= ', result)
            case 11:
                break
            case _:
                print('error')
    else:
        if 1 <= i <= 5:
            y = input1()
        match i:
            case 1:
                result = add(result, y)
                print(expression, '= ', result)
            case 2:
                result = sub(result, y)
                print(expression, '= ', result)
            case 3:
                result = myltiple(result, y)
                print(expression, '= ', result)
            case 4:
                result = division(result, y)
                if y != 0:
                    print(expression, '= ', result)
            case 5:
                result = degree(result, y)
                print(expression, '= ', result)
            case 6:
                result = square(result)
                print(expression, '= ', result)
            case 7:
                result = cube(result)
                print(expression, '= ', result)
            case 11:
                break
            case 12:
                expression = ''
                result = 0
            case _:
                print('error')
