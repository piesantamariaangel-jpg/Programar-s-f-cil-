#Autor: Angel Pie Santamaria
#Data: 9/11/2026
#Curs: 1r ASIX
#Descripció: Es fa servir un bucle per icalcular la suma de tots el nombres y la funció try per indicar si hi han errors
#Especificacions d'entrada: Un numero 
#--------

try: 
    numero = int(input("introdueix un numero"))

    n = numero

    suma = sum(range(1, n+1))
    print(suma)

except ValueError:
    print("Error: El numero ha de ser enter")