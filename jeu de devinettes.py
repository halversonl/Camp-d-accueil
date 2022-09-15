import random


nombre = random.randint(1,100)

essai = -1

nombreEssais = 0

#Tant que la réponse n'est pas correcte, redemander l'utilisateur et ajouter un essai
while(essai != nombre):
        essai = int(input('Quel est mon numero?: '))
        nombreEssais = nombreEssais + 1
                
        if(essai==nombre):
            print("Bravo, tu as gagne! Tu l'as eu en " + str(nombreEssais) + " essais.")
        elif(essai not in range(100)):
             print("S'il vous plait entrer un nombre entre 1 et 100.")
             nombreEssais = nombreEssais - 1
        elif(essai < nombre):
            print('Mon nombre est superieur a cela.')
        elif(essai > nombre):
            print('Mon nombre est inferieur a cela.')
        

 
