num = 1
while num == 1:
    operation = input('Введи операцию (+, -, *, **, //, /, %) ')
    if operation == 'стоп':
        break
    num1 = float(input('Введи первое число '))
    num2 = float(input('Введи второе число '))
    if operation == '+':
        print(float(num1) + float(num2))
    elif operation == '/' and num2 == 0:
        print('На 0 делить нельзя!')
    elif operation == '-':
        print(float(num1) - float(num2))
    elif operation == '*':
        print(float(num1) * float(num2))
    elif operation == '**':
        print(float(num1) ** float(num2))
    elif operation == '//':
        print(float(num1) // float(num2))
    elif operation == '/':
        print(float(num1) / float(num2))
    elif operation == '%':
        print(float(num1) % float(num2))
    elif operation != '//' or operation != '/' or operation != '%' or operation != '//' or  operation != '+' or operation != '-' or operation != '*':
        print('Неверный знак операции!')