# coding:utf-8

print("""
--------------------------------
| Console en ligne de commande |
|       Par jeremx.dev         |
--------------------------------
""")

commands = ["help", "quit", "hello", "operation", "prompt"]

def help():
    print(commands)

def quit():
    exit()

def hello():
    print("Hello World!")

def operation():
    operator = input("Choisir un opérateur (+ ou - ou * ou /) : ")

def prompt():
    prompt = input("Entrer du texte --> ")
    print(prompt)

    try:
        if operator == "+":
            print("Bien, vous avez choisis l'addition!") 
            operanteOne = input("Choisir un nombre : ")
            operanteOne = int(operanteOne)
            operanteTwo = input("Choisir un deuxième nombre : ")
            operanteTwo = int(operanteTwo)
            print(f"Le résultat est : {operanteOne + operanteTwo}")
        elif operator == "-":
            print("Bien, vous avez choisis la soustraction!")
            operanteOne = input("Choisir un nombre : ")
            operanteOne = int(operanteOne)
            operanteTwo = input("Choisir un deuxxième nombre : ")
            operanteTwo = int(operanteTwo)
            print(f"Le résultat est : {operanteOne - operanteTwo}")
        elif operator == "*":
            print("Bien, vous avez choisis la multiplication!")
            operanteOne = input("Choisir un nombre : ")
            operanteOne = int(operanteOne)
            operanteTwo = input("Choisir un deuxième nombre : ")
            operanteTwo = int(operanteTwo)
            print(f"Le résultat est : {operanteOne * operanteTwo}")
        elif operator == "/":
            print("Bien, vous avez choisis la divison!")
            operanteOne = input("Choisir un nombre : ")
            operanteOne = int(operanteOne)
            operanteTwo = input("Choisir un deuxième nombre : ")
            operanteTwo = int(operanteTwo)
            print(f"Le résultat est : {operanteOne / operanteTwo}")
    except ValueError:
        print("Erreur de la valeur saisie!")
    except TypeError:
        print("Erreur du type de la saisie")
    except:
        print("Error générale")

while True:
    commandPrompt = input("Choisir une commande (help... par exemple) : ")
    if commandPrompt == "help":
        help()
    elif commandPrompt == "quit":
        quit()
    elif commandPrompt == "hello":
        hello()
    elif commandPrompt == "operation":
        operation()
    elif commandPrompt == "prompt":
        prompt()
