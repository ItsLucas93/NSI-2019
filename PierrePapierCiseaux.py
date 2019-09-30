from random import choice

print("\n-----------------------------------------------")
print("Bienvenue au jeu du Pierre - Papier - Ciseaux !")
print("-----------------------------------------------\n")


def choixjoueur():
    playerchoice = input('Donnez votre choix entre : \nPierre \nPapier \nCiseaux \n')
    while playerchoice not in ['Pierre', 'Papier', 'Ciseaux']:
        print("\n-----------------------------------------------")
        print("Entrée Incorrecte !")
        print("-----------------------------------------------\n")
        playerchoice = input('Pierre \nPapier \nCiseaux \n')
    return playerchoice


def choixordi():
    return choice(['Pierre', 'Papier', 'Ciseaux'])


a = choixjoueur()

b = choixordi()
print("---------------------- \nL'ordinateur a choisi :", b)

# POSSIBILITE N°1

if a == 'Pierre' and b == 'Ciseaux':
    print("\n-----------------------------------------------")
    print('Vous avez gagné ! \nLa partie prend fin...')
    print("-----------------------------------------------\n")

elif a == 'Pierre' and b == 'Papier':
    print("\n-----------------------------------------------")
    print('Vous avez perdu... :c \nLa partie prend fin...')
    print("-----------------------------------------------\n")

elif a == 'Pierre' and b == 'Pierre':
    print("\n-----------------------------------------------")
    print('Egalité ! \nLa partie prend fin...')
    print("-----------------------------------------------\n")

# POSSIBILITE N°2

if a == 'Papier' and b == 'Pierre':
    print("\n-----------------------------------------------")
    print('Vous avez gagné ! \nLa partie prend fin...')
    print("-----------------------------------------------\n")

elif a == 'Papier' and b == 'Ciseaux':
    print("\n-----------------------------------------------")
    print('Vous avez perdu... :c \nLa partie prend fin...')
    print("-----------------------------------------------\n")

elif a == 'Papier' and b == 'Papier':
    print("\n-----------------------------------------------")
    print('Egalité ! \nLa partie prend fin...')
    print("-----------------------------------------------\n")


# POSSIBILITE N°3

if a == 'Ciseaux' and b == 'Papier':
    print("\n-----------------------------------------------")
    print('Vous avez gagné ! \nLa partie prend fin...')
    print("-----------------------------------------------\n")

elif a == 'Ciseaux' and b == 'Pierre':
    print("\n-----------------------------------------------")
    print('Vous avez perdu... :c \nLa partie prend fin...')
    print("-----------------------------------------------\n")

elif a == 'Ciseaux' and b == 'Ciseaux':
    print("\n-----------------------------------------------")
    print('Egalité ! \nLa partie prend fin...')
    print("-----------------------------------------------\n")
