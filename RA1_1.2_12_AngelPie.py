frase = input("Introdueix una frase") #Demano al usuari que introdueixi una frase
paraula_substituir = input("Introdueix la paraula a substituir") #Demano al usuari que introdueixi la paraula que vol substituir
paraula_nova = input("Introdueix la paraula nova") #Demana al usuari una paraula nova
frase_nova = frase.replace (paraula_substituir, paraula_nova) #Substituixo la paraula per la nova
print(frase_nova) #Ho imprimeixo per pantalla