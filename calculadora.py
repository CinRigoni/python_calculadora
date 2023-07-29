#MENU

while True:

    '''Mostramos al usuario las operaciones que puede realizar'''
    print('Seleccione la operación que desea realizar.')
    print('1 - Suma\n2 - Resta\n3 - Multiplicación\n4 - División')

    '''Capturamos la opción ingresada por el usuario'''
    opcion = input('Opción: ')

    '''Verificamos si la opcion ingresada es válida'''
    if opcion in ('1','2','3','4'):
        '''Pedimos al usario que ingrese los operandos'''
        num1 = float(input('Ingrese el primer número a operar: '))
        num2 = float(input('Ingrese el segundo número a operar: '))

        if opcion == '1':
            print(f'{num1} + {num2} = SUMA')
        elif opcion == '2':
            print(f'{num1} - {num2} = RESTA')
        elif opcion == '3':
            print(f'{num1} * {num2} = MULTIPLICACION')
        elif opcion == '4':
            print(f'{num1} / {num2} = DIVISION')

    else:
        print('Opción inválida.')

    '''Condicion de salida'''
    salir = input('Queres seguir operando? Para salir ingrese la letra X, de lo contrario ingrese cualquier letra: ')

    if salir == 'X' or salir == 'x':
        break
    else:
        continue
    