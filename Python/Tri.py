#Encoding  = UTF-8
#Author  = Lucas 1.6
#Date = 09.12.2019 16:01

import csv

contenu = csv.reader(open('./test4.csv'), delimiter=';')
colonne = []

#Importation de la colonne CSV 

for i in range(0,1):
    for j in contenu:
        colonne.append(j[i])

print(colonne)

#Changer de STR to INT

for i in range(len(colonne)):
    x = 0
    while x < len(colonne):
        colonne[i] = int(colonne[i])
        x = x + 1 

#Tri la liste

for i in range(1,len(colonne)):
    y = colonne[i]
    z = i
    while z > 0 and colonne[z-1] > y :
        colonne[z] = colonne[z-1]
        z = z - 1
    colonne[z] = y 

print(colonne)