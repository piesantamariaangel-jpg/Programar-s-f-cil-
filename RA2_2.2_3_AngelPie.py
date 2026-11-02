#Autor: Angel Pie Santamaria
#Data: 2/11/2026
#Curs: 1r ASIX
#Descripció: Calcula la taula de multiplicar d'un numero del 1 al 10
#Especificacions d'entrada: Numero enter
#--------

numero = int(input("Introdueix un número enter: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
