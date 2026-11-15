#Autor: Angel Pie Santamaria
#Data: 15/11/2026
#Curs: 1r ASIX
#Descripció: Es fa servir un bucle per mostrar els numeros parells desde 0 fins el numero introduït per l'usuari i la funció try per detectar errors 
#Especificacions d'entrada: Un numero 
#--------

try: 
    numero = int(input("introdueix un numero"))

    for i in range(0, numero + 1, 2):
        print(i)

except ValueError:
    print("Error: El numero ha de ser enter")  