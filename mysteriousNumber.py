from random import *

print("Jeu du numéro mystère!")

mysteriousNumber = randrange(0, 50)

print(mysteriousNumber)

game = True
while game:
    enterNumber = input("Quel est le numéro mystère? : ")
    if enterNumber == mysteriousNumber:
        print("Bien jouer !")
        replay = input("Veux-tu rejouer? : ")
        if replay == "oui":
            continue
        else:
            break