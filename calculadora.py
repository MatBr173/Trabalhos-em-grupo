import math
def adc(x, y):
    return x + y

def sub(x,y):
    return x - y
    
def multi(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Tentando dividir por zero? Burro.')

def division_int(x, y):
    try:
        return x // y
    except ZeroDivisionError:
        print('Tentando dividir por zero? Burro.')    

def rest(x, y):
    return x % y

def exp(x, y):
    return x ** y

def sqrt_math(x, y):
    print(f'A raiz de {x} é {math.sqrt(x)}')
    print(f'A raiz de {y} é {math.sqrt(y)}')
    return

def q(item):
    if item == 'y':
        exit() 

while True:
    operadores_validos = ['+','-','*','**','%','/', '//', 'raiz']
    valor_1 = float(input("Digite um valor: "))
    valor_2 = float(input("Digite outro valor: "))
    operador = input("Digite um valor aritimetico (+, -, *, /, //, %, **, raiz, sair): ")
        
    
    if operador not in operadores_validos:
        print('Esse operador não existe')

    commands = {
        '+': lambda: adc(valor_1, valor_2),
        '-': lambda: sub(valor_1, valor_2),
        '*': lambda: multi(valor_1, valor_2),
        '/': lambda: division(valor_1, valor_2),
        '//': lambda: division_int(valor_1, valor_2),
        '%': lambda: rest(valor_1, valor_2),
        '**': lambda: exp(valor_1, valor_2),
        'raiz': lambda: sqrt_math(valor_1, valor_2), 
    }
    if operador not in commands:
        print('Esse operador não existe')

    else:
        try:
            print(commands[operador]())
        except:
            print('NaN') 

    sair = input('Deseja sair? (Y/N): ').lower().replace(' ', '')
    q(sair)