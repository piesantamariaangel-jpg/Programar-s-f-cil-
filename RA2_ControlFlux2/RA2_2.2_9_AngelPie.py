#Autor: Angel Pie Santamaria
#Data: 2/11/2026
#Curs: 1r ASIX
#Descripció: Troba el nuúmero màxim d'una llista de números
#Especificacions d'entrada: Llista de números
#--------


numeros = input("Introdueix diversos números separats per espais: ")

llista = numeros.split()

maxim = int(llista[0])

for numero in llista:
    numero = int(numero)

    if numero > maxim:
        maxim = numero

print("El número màxim és:", maxim)
