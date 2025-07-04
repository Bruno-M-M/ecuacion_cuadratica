from funciones import discriminante
from funciones import soluciones
from funciones import concavidad
from funciones import vertice
from funciones import raices

def main():
    try:
        a = float(input("Ingrese valor de a: "))
        b = float(input("Ingrese valor de b: "))
        c = float(input("Ingrese valor de c: "))
    except ValueError:
        print("debe ingresar valores numericos")
    if a == 0:
        return "El valor no puede ser cero"
    
    resultado = {}

    while True:
        try:
            print("Menú:\n1) Calcular discriminante\n2) Calcular soluciones\n3) Dirección de la parábola\n4) Calcular vértice\n5) Tipo de raíces\n6) Mostrar todos los resultados guardados\n7) Salir")
            opcion = int(input("ingrese una de las opciones"))
            if 0 < opcion < 8:
                print("Opcion valida")
                if opcion == 1:
                    d = discriminante(a,b,c)
                    resultado["discriminante"] = d
                elif opcion == 2:
                    h = soluciones(a,b,c)
                    resultado["soluciones"] = h
                elif opcion == 3:
                    l = concavidad(a)
                    resultado["concavidad"] = l
                elif opcion == 4:
                    v = vertice(a,b,c)
                    resultado["vertice"] = v
                elif opcion == 5:
                    r = raices(a,b,c)
                    resultado["raices"] = r
                elif opcion == 6:
                    print(resultado)
                elif opcion == 7:
                    print("Finalizando programa")
                    break
                else:
                    print("no existe esa opcion")
            else:
                print("opcion ingresada invalida")
        except ValueError:
            print("debe ingresar una opcion numerica")

main()
