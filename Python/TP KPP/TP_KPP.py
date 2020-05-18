import time
start_time = time.time()

from math import sqrt
import csv
from pylab import *


##############################TRAVAIL PREPARATOIRE TP (FONCTIONS DE BASE)#####################################

def distance(pointA, pointB):
    xA, yA = pointA
    xB, yB = pointB
    return sqrt((xB - xA) ** 2 + (yB - yA) ** 2)


def Moyenne(L):
    """Calcul de la moyenne """
    return sum(L) / len(L)


def Covariance(L1, L2):
    Li = [(L1[i] - Moyenne(L1)) * (L2[i] - Moyenne(L2)) for i in range(len(L1))]
    return sum(Li) / len(L1)


def Variance(L):
    Li = [(x - Moyenne(L)) ** 2 for x in L]
    return sum(Li) / len(L)


def EcartType(L1):
    return sqrt(Variance(L1))


def Somme(L1):
    somme = 0
    for i in range(0, len(L1)):
        somme = somme + L1[i]
    return somme


def alpha(L1, L2):
    a = ((len(L1) * Covariance(L1, L2)) - (Somme(L1) * Somme(L2))) / (
            (len(L1) * Variance(L1)) - (Somme(L1) * Somme(L1)))
    return a


def beta(L1, L2):
    b = Moyenne(L2) - (Moyenne(L1) * alpha(L1, L2))
    return b


def Regression_lineaire(L1, L2):
    alpha = ((len(L1) * Covariance(L1, L2)) - (Somme(L1) * Somme(L2))) / (
            (len(L1) * Variance(L1)) - (Somme(L1) * Somme(L1)))
    beta = Moyenne(L2) - (Moyenne(L1) * alpha)
    return alpha, beta


# Fonctions tri

def tri(t):
    n = len(t)
    if n < 2:
        return t
    else:
        m = n // 2
    return fusion(tri(t[:m]), tri(t[m:]))


def fusion(t1, t2):
    if t1 == []:
        return t2
    elif t2 == []:
        return t1
    elif t1[0] < t2[0]:
        return [t1[0]] + fusion(t1[1:], t2)
    else:
        return [t2[0]] + fusion(t1, t2[1:])


##############################PARTIE 1#####################################

# on place les points sur le graphe


def k_proches_voisins(data, origine, k):
    reponse = []
    for propriete in data.keys():
        for voisin in data[propriete]:
            d = distance(origine, voisin)
            # Insertion dans la liste des k plus proches voisins
            i = 0
            while i < k and i < len(reponse) and reponse[i][0] <= d:
                i += 1
            if i < k:
                reponse.insert(i, (d, propriete))
    return reponse[:k]


def categorie_devine(data, origine, k):
    liste_cles = list(data.keys())
    tri = [[0, 0, p] for p in liste_cles]
    kpv = k_proches_voisins(data, origine, k)
    for distance, propriete in kpv:
        i = liste_cles.index(propriete)
        tri[i][0] -= 1
        tri[i][1] += distance
    return min(tri)[2]


##################################################################

# Importation des valeurs
with open("./dataetoile_REf.csv", newline='') as monFichier:
    monContenu_Ref = csv.reader(monFichier, delimiter=";")
    # Création des listes correspondantes
    position1_Ref = [];
    position2_Ref = [];
    etoile_Ref = [];
    temperature_Ref = [];
    masse_Ref = [];
    for row in monContenu_Ref:
        position1_Ref.append(float(row[0].replace(",", ".")))
        position2_Ref.append(float(row[1].replace(",", ".")))
        etoile_Ref.append(float(row[2].replace(",", ".")))
        temperature_Ref.append(float(row[3].replace(",", ".")))
        masse_Ref.append(float(row[4].replace(",", ".")))

with open("./dataetoile.csv", newline='') as monFichier_2:
    monContenu = csv.reader(monFichier_2, delimiter=";")

    position1 = [];
    position2 = [];
    etoile = [];
    temperature = [];
    masse = [];
    for row in monContenu:
        position1.append(float(row[0].replace(",", ".")))
        position2.append(float(row[1].replace(",", ".")))
        etoile.append(float(row[2].replace(",", ".")))
        temperature.append(float(row[3].replace(",", ".")))
        masse.append(float(row[4].replace(",", ".")))


#########################QUESTION 1#########################################

def DIM(L):
    produit = []
    for i in L:
        produit.append(30 * i)
    return produit


#########################QUESTION 2#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 2-*-*-*-*-*-*-*-*-*-*-*-*-")

dico_Ref = {}
for x in range(10):
    dico_Ref.update({str(x + 1): [(temperature_Ref[x], masse_Ref[x])]})

assemblage = []
for x in range(len(dico_Ref)):
    l = []
    assemblage.append(l)

for x in range(len(position1)):
    res = categorie_devine(dico_Ref, (temperature[x], masse[x]), 10)
    a = 1
    while res != str(a):
        a += 1
    assemblage[a - 1].append(int(etoile[x]))

for x in range(len(dico_Ref)):
    print("Position étoile type ", x + 1, " :", assemblage[x])

#########################QUESTION 3#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 3-*-*-*-*-*-*-*-*-*-*-*-*-")

for x in range(len(assemblage)):
    if len(assemblage[x]) != 0:
        print("Type d'étoile n°", x + 1, " est à : ", (len(assemblage[x]) / 40) * 100, "%")

#########################QUESTION 4#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 4-*-*-*-*-*-*-*-*-*-*-*-*-")


def classement_temperature(temperature):
    tri_temperature = tri(temperature)
    tri_2 = []
    for i in range(len(temperature)):
        x = temperature.index(tri_temperature[i])
        tri_2.append([position1[x], position2[x], etoile[x], temperature[x], masse[x]])
    return tri_2


print("Classement des température des étoiles par ordre croissant", classement_temperature(temperature))

#########################QUESTION 5#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 5-*-*-*-*-*-*-*-*-*-*-*-*-")


def data_etoile_tri(i):
    file_name = open("./data_etoile_tri.csv", "w")
    for x in i:
        ligne = str(x) + "\n"
        file_name.write(ligne)


data_etoile_tri(classement_temperature(temperature))
print("Création du fichier effectué ! Il se trouve dans le dossiez auquel vous executez le fichier actuel.")

#########################QUESTION 6#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 6-*-*-*-*-*-*-*-*-*-*-*-*-")


def Pearson(L1, L2):
    return Covariance(L1, L2) / (EcartType(L1) * EcartType(L2))


masse_temp_1 = []
temperature_temp_1 = []

for x in range(len(dico_Ref)):
    temperature_temp_1.append([])
    masse_temp_1.append([])

for x in range(len(assemblage)):
    for i in range(len(assemblage[x])):
        if assemblage[x] != []:
            a = assemblage[x][i]
            masse_temp_1[x].append(masse[a - 1])
            temperature_temp_1[x].append(temperature[a - 1])

moyenne_masse = []
moyenne_temperature = []
n = 0

for x in range(len(masse_temp_1)):
    if masse_temp_1[x] != []:
        n = Moyenne(masse_temp_1[x])
        moyenne_masse.append(n)
        n = Moyenne(temperature_temp_1[x])
        moyenne_temperature.append(n)
    else:
        moyenne_masse.append(0)
        moyenne_temperature.append(0)

print("Moyenne de la masse par type d'étoile : ", moyenne_masse)
print("moyenne de la température par type d'étoile : ", moyenne_temperature)
print("Résultat Pearson :", Pearson(temperature, masse))

#########################QUESTION 7#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 7-*-*-*-*-*-*-*-*-*-*-*-*-")

masse_temp_2 = []
temperature_temp_2 = []

for i in range(len(masse_temp_1)):
    if masse_temp_1[i] != []:
        masse_temp_2.append(masse_temp_1[i])
        temperature_temp_2.append(temperature_temp_1[i])

rangs = [3, 4, 5, 6, 9, 10]
for i in range(len(masse_temp_2)):
    print("La régression linéaire du type n°", rangs[i], "est :", Regression_lineaire(temperature_temp_2[i], masse_temp_2[i]))
    print("La correlation linéaire du type n°", rangs[i], "est :", Pearson(temperature_temp_2[i], masse_temp_2[i]), "\n")

del temperature_temp_2, masse_temp_2, temperature_temp_1, masse_temp_1
#########################QUESTION 8#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 8-*-*-*-*-*-*-*-*-*-*-*-*-")

print("La régression linéaire des moyennes des temperatures et masses pour les types d'étoiles ",
      Regression_lineaire(moyenne_temperature, moyenne_masse))

#########################QUESTION 9#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 9-*-*-*-*-*-*-*-*-*-*-*-*-")
L1 = moyenne_temperature
L2 = moyenne_masse
alpha = ((len(L1) * Covariance(L1, L2)) - (Somme(L1) * Somme(L2))) / (
        (len(L1) * Variance(L1)) - (Somme(L1) * Somme(L1)))
beta = Moyenne(L2) - (Moyenne(L1) * alpha)
print("L'équation de régression linéaire est : ", alpha, "* x +", beta)
print("Le coefficient de corrélation des moyennes des temperatures et masses pour les types d'étoiles est :",
      Pearson(moyenne_temperature, moyenne_masse))

print("Temps d'execution : %s secondes ---" % (time.time() - start_time)) # Temps d'execution : 0.4244239330291748 secondes ---

#########################QUESTION 10#########################################

print("-*-*-*-*-*-*-*-*-*-*-*-*-Question 10-*-*-*-*-*-*-*-*-*-*-*-*-")

color = ['w', 'r', 'y', 'm', 'b', 'coral', 'orange', 'darkviolet', 'pink', 'gold']

masse_log = []
for x in masse:
    masse_log.append(math.log(x))

temperature_log = []
for x in temperature:
    temperature_log.append(math.log(x / 4200))


def figure(p1, p2, s, c, title, xlabel, ylabel, background, filename):
    plt.figure()
    plt.scatter(p1, p2, s=s, c=c)
    plt.style.use([background])
    plt.title(title, c="white")
    plt.xlabel(xlabel, c="white")
    plt.ylabel(ylabel, c="white")
    plt.savefig(filename + '.png')
    print("Fichier '" + filename + '.png' + "' crée dans le dossier d'éxcecution.")


figure(masse, temperature, 100, 'r', 'analyse1', 'masse', 'temperature', 'dark_background', 'graph')
figure(position1_Ref, position2_Ref, DIM(masse_Ref), color, 'Étoile de référence', 'position1_Ref', 'position2_Ref', 'dark_background' ,'Graph : Référence')
# Question 10A
figure(position1, position2, DIM(masse), color*4, 'Carte du ciel', 'position1', 'position2', 'dark_background', 'Graph : Carte du ciel')

# Question 10B
masse_log = []
for x in masse:
    masse_log.append(math.log(x))

temperature_log = []
for x in temperature:
    temperature_log.append(math.log(x / 5900))


figure(masse_log, temperature_log, DIM(masse), color*4, 'Log(Température/température) en fonction des log(masse)', 'log(masses)', 'log(Température/température)','dark_background' , 'Graph : Log_Température en fonction de Log_Masse')

# Question 10C
figure(moyenne_masse, moyenne_temperature, DIM(masse_Ref), color, 'Moyenne Masse/Température', 'Masse', 'Température', 'dark_background' , 'Graph : Moyenne masse_température')


print("Temps d'execution : %s secondes ---" % (time.time() - start_time)) # Temps d'execution : 1.1886091232299805 secondes ---
