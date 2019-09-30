# Auteurs : Lucas | Bilal 1ère 6 Persée
# ----------------------------------------------------------

from math import *  # Import pour la fonction de racine carrée
import numpy as np  # Import des modules pour tracer la courbe, attribution d'aliases (raccourcis de noms)
import matplotlib.pyplot as plt


def SolEq1():
    print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("SolEq1")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    print("Programme qui calcule les racine et le delta d'un polynôme du 2nd degré.")
    print("Ax² + Bx + C = 0")

    print("-------------------------------------------------")

    print("Entrez les valeurs de A, puis de B, puis de C.\n"
          "Si vous entrez une valeur qui n'est pas une valeur numérique, le programme s'arêtera.\n")

    A = input("Valeur de A : ")
    B = input("Valeur de B : ")
    C = input("Valeur de C : ")

    A = int(A)
    B = int(B)
    C = int(C)

    print("Les valeurs entrées sont : A = [", A, "], B = [", B, "], C = [", C, "]")

    print("-------------------------------------------------")
    # Calcul de Delta en fonction de A, B, C

    delta = B * B - 4 * A * C
    print("Valeur de Delta (discriminant) calculée en fonction de A, B, C : ", delta)

    if delta > 0:  # Lorsque delta est positif, il y a donc deux solutions, x1 et x2.
        print("Delta est positif, il y a donc deux solutions.")  # Envoie à l'utilisateur qu'il y a donc deux solutions
        rc_delta = sqrt(delta)  # Racine carrée de Delta
        numerateur_x1 = -B - rc_delta  # Numérateur de x1
        numerateur_x2 = -B + rc_delta  # Numérateur de x2
        denominateur = 2 * A  # Dénominateur de x1 et x2
        x1 = numerateur_x1 / denominateur  # Calcul de x1
        x2 = numerateur_x2 / denominateur  # Calcul de x2
        print("Valeur de x1 = ", x1)  # Résultat de x1
        print("Valeur de x2 = ", x2)  # Résultat de x2
        print("\nFin du programme.")

    if delta == 0:  # Lorsque delta est nul, il n'y a donc qu'une seule solution.
        print("Delta est a une valeur nulle, il y a donc seulement une seule solution. ")
        # Envoie à l'utilisateur qu'il y a donc qu'une seule solution
        x0 = -B / 2 * A  # Calcul de x0
        print("Valeur de x0 = ", x0)  # On affiche la solution
        print("\nFin du programme.")

    if delta < 0:  # Lorsque delta est négative, il n'y a donc pas de solution possible.
        print("Delta est négatif, il n'y a donc pas de solution possible. \nFin du programme.")
        # Envoie à l'utilisateur qu'il n'y a pas de solution.a

    print("-------------------------------------------------")


def SolEq2():
    print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("SolEq2")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    print("-------------------------------------------------")

    print("Programme qui calcule les racine et le delta d'un polynôme du 2nd degré.")
    print("Ax² + Bx + C = 0")

    print("-------------------------------------------------")

    value_eq2 = input("Entrez les valeurs de A, puis B, puis C en veillant à laisser seulement un espace entre les "
                      "valeurs. \n"
                      "Si vous entrez une valeur qui n'est pas une valeur numérique, le programme s'arêtera.\n").split(
        " ")

    print("Les valeurs entrées sont : A = [", value_eq2[0], "], B = [", value_eq2[1], "], C = [", value_eq2[2], "]")

    # Réatribution des valeurs A, B, C aux variables A, B, C

    A = int(value_eq2[0])
    B = int(value_eq2[1])
    C = int(value_eq2[2])

    print("-------------------------------------------------")
    # Calcul de Delta en fonction de A, B, C

    delta = B * B - 4 * A * C
    print("Valeur de Delta (discriminant) calculée en fonction de A, B, C : ", delta)
    list_delta = [delta]

    if delta > 0:  # Lorsque delta est positif, il y a donc deux solutions, x1 et x2.
        print("Delta est positif, il y a donc deux solutions.")  # Envoie à l'utilisateur qu'il y a donc deux solutions
        rc_delta = sqrt(delta)  # Racine carrée de Delta
        numerateur_x1 = -B - rc_delta  # Numérateur de x1
        numerateur_x2 = -B + rc_delta  # Numérateur de x2
        denominateur = 2 * A  # Dénominateur de x1 et x2
        x1 = numerateur_x1 / denominateur  # Calcul de x1
        x2 = numerateur_x2 / denominateur  # Calcul de x2
        print("Valeur de x1 = ", x1)  # Résultat de x1
        print("Valeur de x2 = ", x2)  # Résultat de x2
        list_x = [round(x1, 2), round(x2, 2)]
        print("Les solutions sont :", list_x, "\nLa valeur de Delta est : ", list_delta)
        print("\nFin du programme.")

    if delta == 0:  # Lorsque delta est nul, il n'y a donc qu'une seule solution.
        print("Delta est a une valeur nulle, il y a donc seulement une seule solution. ")
        # Envoie à l'utilisateur qu'il y a donc qu'une seule solution
        x0 = -B / 2 * A  # Calcul de x0
        print("Valeur de x0 = ", x0)  # On affiche la solution
        list_x0 = [round(x0, 2)]
        print("La solutions est :", list_x0, "\nLa valeur de Delta est : ", list_delta)
        print("\nFin du programme.")

    if delta < 0:  # Lorsque delta est négative, il n'y a donc pas de solution possible.
        print("Delta est négatif, il n'y a donc pas de solution possible. \nFin du programme.")
        # Envoie à l'utilisateur qu'il n'y a pas de solution.a

    print("-------------------------------------------------")


def fx_courbe():
    # Rappel : f(x) = x + 2
    # f(-2) = 0
    # f(-1) = 1
    # f(0) = 2
    # f(1) = 3
    x = np.array([-2, -1, 0, 1])
    y = np.array([0, 1, 2, 3])
    plt.plot(x, y)

    plt.show()  # Affiche la courbe


def listecomprehension():
    print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("Compréhension de liste (Exercice dans le code)")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    print("\n")
    # Une compréhension de liste est une simplification d'une transformation d'une liste 1 en une liste 2
    # Exemple :
    liste_1 = [0, 1, 2, 3, 4, 5]
    liste_2 = []
    for n in liste_1:
        liste_2.append(n * 2)
    print(liste_2)
    # Le résultat sera : [0, 2, 4, 6, 8, 10]
    print("-------------------------------------------------")
    # Tout cela peut-être simplifié en :
    liste_3 = [0, 1, 2, 3, 4, 5]
    liste_4 = [n * 2 for n in liste_3]
    print(liste_4)
    # Le résultat sera encore une fois : [0, 2, 4, 6, 8, 10]
    # On vient d'économiser 1 ligne de code pour
    # la rendre plus compacte, plus simple, plus compréhensible, plus rapide à écrire.
    print("-------------------------------------------------")


def listeinitiale():
    print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("Liste initiale (Exercice dans le code)")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    liste_initiale = [0, 1, 2, 3, 4, 5]
    liste_2 = [n * 2 for n in liste_initiale]
    print(liste_2)
    # Peut s'écrire
    liste_initiale = [0, 1, 2, 3, 4, 5]
    liste_2 = []
    for n in liste_initiale:
        liste_2.append(n * 2)
    print(liste_2)


def main():  # Réalise une demande pour le choix de la fonction à executer.
    print("-------------------------------------------------")
    entree = input("Bonjour ! Quel est la fonction demandé ?"
                   "\n\n1 = SolEq1 : "
                   "Coder un fonction SolEqua1(a,b,c) qui retourne les valeurs des solutions et discriminant."
                   "\n\n2 = SolEq 2 : "
                   "Coder une fonction SolEqua2(liste) "
                   "qui retourne les valeurs des solutions et du discriminant sous forme de liste."
                   "\n\n3 = fxcourbe : "
                   "Faire une recherche permettant de tracer une courbe défini comme f(x)=x+2"
                   "\n\n4 = listecomprehension : "
                   "Faire une recherche sur les listes en compréhension. "
                   "Analyser l'instruction suivante et dire l'intérêt d'une telle écriture."
                   "\n\n5 = listeinitiale : "
                   "Proposer une autre écriture qui donne le même résultat. "
                   "\n\n-------------------------------------------------\nDemande = ")
    print("-------------------------------------------------")

    entree = int(entree)

    if entree == 1:
        SolEq1()
    if entree == 2:
        SolEq2()
    if entree == 3:
        fx_courbe()
    if entree == 4:
        listecomprehension()
    if entree == 5:
        listeinitiale()
    else:
        print("Erreur, le programme à mis fin soit parce que la demande a été traité, soit que vous ayez rentrée une "
              "valeur incorrect/demande inexistante. \nFin du programme.")
        print("-------------------------------------------------")


main()
