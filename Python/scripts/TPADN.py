# KOCOGLU Lucas et ABEDLI Bilal 1.6 Persée
# TP ADN

# EX1

Brin_non_codant1 = ["ATCGTGCTGCTGCGGTGCGCGCGGCGGCGTGCGAAGAACGGCGGCGGCGGCGGCGGCGGCGGTGGTGGTGGTTCTTCTTCTTCTTCTTCGTA"]
brin_compl = []
for i in Brin_non_codant1:
    for n in i:
        if n == "A":
            n = "T"
        elif n == "T":
            n = "A"
        elif n == "G":
            n = "C"
        elif n == "C":
            n = "G"
        brin_compl.append(n)

print("Brin Complémentaire = ", brin_compl)

# EX 2

ARNm = []
for i in Brin_non_codant1:
    for n in i:
        if n == "A":
            n = "U"
        elif n == "T":
            n = "A"
        elif n == "G":
            n = "C"
        elif n == "C":
            n = "G"
        ARNm.append(n)

print("ARNm = ", ARNm)

# EX 3

code1 = {"UUU": "F", "UUC": "F",
         "UUA": "L", "UUG": "L",
         "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
         "UAU": "Y", "UAC": "Y",
         "UAA": "STOP", "UAG": "STOP",
         "UGU": "C", "UGC": "C",
         "UGA": "STOP",
         "UGG": "W",
         "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
         "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
         "CAU": "H", "CAC": "H",
         "CAA": "Q",
         "CAG": "Q",
         "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
         "AUU": "I", "AUC": "I", "AUA": "I",
         "AUG": "START",
         "ACU": "U", "ACC": "U", "ACA": "U", "ACG": "U",
         "AAU": "N", "AAC": "N",
         "AAA": "K", "AAG": "K",
         "AGU": "S", "AGC": "S",
         "AGA": "R", "AGG": "R",
         "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
         "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
         "GAU": "D", "GAC": "D",
         "GAA": "E", "GAG": "E",
         "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
         }

code2 = {

    "F": ["UUU", "UUC"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG", ],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "Y": ["UAU", "UAC"],
    "STOP": ["UAA", "UAG", "UGA"],
    "C": ["UGU", "UGC"],
    "W": ["UGG"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "H": ["CAU", "CAC"],
    "Q": ["CAA", "CAG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "I": ["AUU", "AUC", "AUA"],
    "START": ["AUG"],
    "U": ["ACU", "ACC", "ACA", "ACG"],
    "N": ["AAU", "AAC"],
    "K": ["AAA", "AAG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "G": ["GGU", "GGC", "GGA", "GGG"],
}

targerkey = code2.get(input("Entrez la clée"))
print("Valeur(s) de la clé : ", targerkey)
