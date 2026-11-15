#Autor: Angel Pie Santamaria
#Data: 15/11/2026
#Curs: 1r ASIX
#Descripció: Es fa servir un bucle per imprimir tots el nombres primers desde 2 fins al numero introduït per l'usuari i la funció try per detectar errors. 
#Especificacions d'entrada: Un numero 
#--------

try:
    numero = int(input("Introduce un número: "))

    for i in range(2, numero + 1):
        es_primo = True

        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break

        if es_primo:
            print(i)

except ValueError:
    print("Error: El número ha de ser entero")