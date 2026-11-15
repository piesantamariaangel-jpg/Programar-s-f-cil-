#Autor: Angel Pie Santamaria
#Data: 9/11/2026
#Curs: 1r ASIX
#Descripció: Es fa servir un bucle per mostrar la taula de multiplicar d'un numero introduït per l'usuari i la funció try per detectar errors 
#Especificacions d'entrada: Un numero 
#--------

try: 
    numero = int(input("introdueix un numero"))

    for i in range(1, 11):
        print(i * numero)

except ValueError:
    print("Error: El numero ha de ser enter")  
