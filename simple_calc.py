
while True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operator = input('Digite a operação desejada (+, -, *, /): ')
    
    num_1_float = 0
    num_2_float = 0
    allowed_operators = '+-/*'
    
    valid_num = True
    
    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_num = True
    except:
        valid_num = None

    if valid_num is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    if len(operator) > 1 :
        print('Digite apenas uma operação.')
        continue

    if operator not in allowed_operators:
        print('Operação inválida.')
        continue

    if operator == '+':
        f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float
    elif operator == '-':
        f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float
    elif operator == '*':
        f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float
    elif operator == '/':
        f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float
    else:
        print(' ')

    exit = input('Deseja sair? [s]im: ').lower().startswith('s')

    if exit:
        break