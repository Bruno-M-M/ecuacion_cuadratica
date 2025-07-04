#menu simple de demostracion
from funcionessimpleejemplo import suma
from funcionessimpleejemplo import resta
from funcionessimpleejemplo import multiplicacion
from funcionessimpleejemplo import division
from funcionessimpleejemplo import salir

def main():
    while True:
        try:
            print("--Calculadora--\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Salir")
            opcion = int(input("Ingrese una opcion de forma numerica\n"))
            if opcion == 1:
                print(suma())
            elif opcion == 2:
                print(resta())
            elif opcion == 3:
                print(multiplicacion())
            elif opcion == 4:
                print(division())
            elif opcion == 5:
                print(salir())
                break
            else:
                print("Debe ingresar una opcion valida")
        except ValueError:
            print("El valor ingresado debe ser entero")

main()