# coding:utf-8

print("""
-----------------------------
| Trouver le numéro mystère |
|       Par jeremx.dev      |
-----------------------------
""")

import random

# Create the mysterious number
mysteriousNumber = random.randrange(0, 50)

print(mysteriousNumber)

game = True

print("Bienvenue sur le jeu du numéro mystère !")

while game:

    try:
        askToTheMysteriousNumber = input("Quel est le numéro mystère ? (compris entre 0 et 50) : ")
        askToTheMysteriousNumber = int(askToTheMysteriousNumber)
    except ValueError:
        print("Tu dois rentrer un nombre entier pour le jeu !")
        continue
    except TypeError:
        print("Le type entré n'est pas prit en charge ! Tu dois rentrer un nombre entier pour le jeu !")
        continue
    if askToTheMysteriousNumber < 0:
        print("Tu dois entrer un numéro compris entre 0 et 50 !")
        continue
    elif askToTheMysteriousNumber > 50:
        print("Tu dois entrer un numéro entre 0 et 50 !")
        continue
    else:
        if askToTheMysteriousNumber != mysteriousNumber:
            print("Dommage ce n'est pas le bon numéro !")
            asKToContinue = input("Veux-tu quand-même continuer à jouer ? (oui ou non) : ")
            if asKToContinue == "oui":
                print("D'accord")
            elif asKToContinue == "non":
                print("D'accord. Au-revoir!")
                break
        elif askToTheMysteriousNumber == mysteriousNumber:
            print("Bravo tu as trouvé le bon numéro !")
            asKToContinue = input("Veux-tu continuer à jouer ? (oui ou non) : ")
            if asKToContinue == "oui":
                print("D'accord")
                continue
            elif asKToContinue == "non":
                print("D'accord. Au-revoir!")
                break