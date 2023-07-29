#FUNCIONES

'''Funcion que recibe como parametros dos numeros y
devuelve la suma de los mismos'''

def suma(a, b):
    return (a+b)

'''Funcion que recibe como parametros dos numeros y
devuelve la resta de los mismos'''

def resta(a, b):
    return (a-b)

'''Funcion que recibe como parametros dos numeros y
devuelve la multiplicacion de los mismos'''

def multiplicacion(a, b):
    return (a*b)

'''Funcion que recibe como parametros dos numeros y
devuelve la division de los mismos'''

def division(a, b):
    if(b == 0):
        return ('No se puede dividir por 0!')
    else:
        return (a/b)

