# Lucas et Bilal 1.6

import csv

contenu = csv.reader(open('./dicho.csv'), delimiter=';')

#def afficheTab(tableauH):
#    for element in tableauH:
#        print(element)

def afficheCol(tab, nbligne):
    for element in tab:
        print(element[nbligne])

afficheCol(contenu, 1)


colonne = []

for row in contenu:
    print(row)

print(colonne)        
    
colonne_list = []

for x in contenu:
    colonne_list.append(int(x[1]))
print(colonne_list)


def imin(T,a,b):
    imin = a
    N = len(T)
    for i in range(a+1,b):
        if  T[i] < T[imin]:
            imin = i
    return imin

def tri_select(T):
    n = len(T)
    for i in range(n-1):
        j = imin(T,i,n)
        T[i], T[j] = T[j], T[i]
        print(T)
    return T

tri_select(colonne_list)
        
        
        
      
