# Encoding  = UTF-8
# Author  = Lucas 1.6
# Date = 16.12.2019 16:14
# Exercice : Count time of an function


import time
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()


def fx_courbe():
    # Rappel : f(x) = x + 2
    # f(-2) = 0
    # f(-1) = 1
    # f(0) = 2
    # f(1) = 3
    x = np.array([-2, -1, 0, 1])
    y = np.array([0, 1, 2, 3])
    plt.plot(x, y)
    plt.title("f(x) = x + 2")
    print("Temps d'execution : %s secondes ---" % (time.time() - start_time))

    plt.show()


fx_courbe()

# --------------------------------------


start_time2 = time.time()
colonne = [2738248, 178538, 836859, 649000, 489937, 151019, 137304, 8080734, 283767, 525389, 110329, 127700, 411706,
           2431649, 100000, 455992, 115564]

# Changer de STR to INT

for i in range(len(colonne)):
    x = 0
    while x < len(colonne):
        colonne[i] = int(colonne[i])
        x = x + 1

    # Tri la liste

for i in range(1, len(colonne)):
    y = colonne[i]
    z = i
    while z > 0 and colonne[z - 1] > y:
        colonne[z] = colonne[z - 1]
        z = z - 1
    colonne[z] = y

print(colonne)
print("Temps d'execution : %s secondes ---" % (time.time() - start_time2))
