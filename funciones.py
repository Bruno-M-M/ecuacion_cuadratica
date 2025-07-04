import math

#funcion discriminante
def discriminante(a,b,c):
    return b**2 - 4*a*c

#funcion de soluciones
def soluciones(a,b,c):
    d = discriminante(a,b,c)
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1,x2
    elif d == 0:
        x = -b/2*a
        return x
    else:
        return "no hay soluciones"

#direccion concavidad
def concavidad(a):
    if a > 0:
        return "Funcion concava hacia arriba"
    elif a < 0:
        return "Funcion concava hacia abajo"
    else:
        return "A debe ser distinto de cero"
    
#vertice de la parabola
def vertice(a,b,c):
    x = -b/2*a
    y = a*(x)**2 + b*x + c
    return (x,y)

#raices
def raices(a,b,c):
    d = discriminante(a,b,c)
    if d > 0:
        return "dos raices distintas"
    elif d == 0:
        return "dos raices iguales"
    else:
        return "dos raices complejas"