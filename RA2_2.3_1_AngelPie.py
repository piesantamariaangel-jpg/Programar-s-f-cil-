#Autor: Angel Pie Santamaria
#Data: 9/11/2026
#Curs: 1r ASIX
#Descripció: Es fa servir un bucle que genera una seqüència i s'utilitza la funció try per inicar que ha de ser un numero enter.
#Especificacions d'entrada: Un numero 
#--------

try: 
    numero = int(input("introdueix un numero"))

    for i in range(0, numero +1):
        print(i)

except ValueError:
    print("Error: El numero ha de ser enter")