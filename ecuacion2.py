#Código base de la ecuación cuadrática funcional.

from cmath import sqrt

print("-------------------------------------")
print("---------Ecuación Cuadrática---------")
print("-------------------------------------")

# input

a = int(input("Digite el término cuadrático: "))
b = int(input("Digite el término lineal: "))
c = int(input("Digite el valor independiente: "))
x1= 0
x2= 0

# processing and ouput

if ((b**2)-4*a*c) < 0:
    print("La solución final hace parte de los números complejos.")

else:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("Las posibles soluciones son: ")
    print(x1)
    print(x2)