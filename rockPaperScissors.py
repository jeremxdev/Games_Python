#coding:utf-8

print("""
-----------------------------------
| Jeu de pierre, feuille, scissos |
|       par jeremx.dev            |
-----------------------------------
""")

from random import *

tools = ["pierre", "feuille", "scissos"]

def Game():
    game = True
    while game:
        computerChoice = choice(tools)
        
        userChoice = input("pierre ?, feuille ?, scissos ? : ")

        if computerChoice == "pierre" and userChoice == "feuille":
            print("Tu as gagné ! La feuille couvre la pierre !")
        elif computerChoice == "feuille" and userChoice == "scissos":
            print("Tu as gagné ! Les scissos coupe la feuille !")
        elif computerChoice == "scissos" and userChoice == "pierre":
            print("Tu as gagné ! La pierre case les scissos !")
        elif computerChoice == "feuille" and userChoice == "pierre":
            print("Tu as perdu ! La feuille couvre la pierre !")
        elif computerChoice == "pierre" and userChoice == "scissos":
            print("Tu as perdu ! La pierre case les scissos !")
        elif computerChoice == "feuille" and userChoice == "pierre":
            print("Tu as perdu ! La feuille couvre la pierre !")
        elif computerChoice == "scissos" and userChoice == "feuille":
            print("Tu as perdu ! Les scissos coupe la feuille !")
        elif computerChoice == userChoice:
            print("Dommage, égalité !")
        else:
            break

Game()  