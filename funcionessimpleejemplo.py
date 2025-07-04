#funciones del menu simple ejemplo

def suma():
    a = int(input("Ingrese primer valor: "))
    b = int(input("Ingrese segundo valor: "))
    resultado = a + b
    return resultado
def resta():
    a = int(input("Ingrese primer valor: "))
    b = int(input("Ingrese segundo valor: "))
    resultado = a - b
    return resultado
def multiplicacion():
    a = int(input("Ingrese primer valor: "))
    b = int(input("Ingrese segundo valor: "))
    resultado = a * b
    return resultado
def division():
    a = int(input("Ingrese primer valor: "))
    b = int(input("Ingrese segundo valor: "))
    resultado = a / b
    return resultado
def salir():
    return "Apagando calculadora\nQue tenga buen dia."