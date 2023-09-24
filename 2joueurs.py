import string
import random
import time
import os
from os import system
os.system('cls')
os.system('color 1F')
S = random.randint(5, 10)  # nombre de caractère aléatoire
m = ''.join(random.choices(string.ascii_uppercase, k=S))  # random string
# m="PY"
print("    ", end="")
joeur1 = input("entrer le nom du joueur 1 :")
joeur1 = joeur1.capitalize()
print("    ", end="")
joeur2 = input("entrer le nom du joueur 2 :")
joeur2 = joeur2.capitalize()
os.system('cls')
mot = []
for i in m:
    mot.append(i)
mot3 = []
for i in m:
    mot3.append(i)
mot2 = []  # ajouter une liste des etoiles
for i in range(len(mot)):
    mot2.append("*")
print()
z = 0
j1 = 0
j2 = 0
while z >= 0:
    z += 1
    print("    ", end="")
    print(" ".join(mot2),)  # ListeToString
    print("    ", end="")
    print(f"{joeur1}:{j2} points")
    print("    ", end="")
    print(f"{joeur2}:{j1} points")
    MaxEssei = len(m)*3
    if mot2 == mot3:  # si le mot est complet
        if j1 > j2:
            os.system('color 2f')
            print(f"    {joeur2} est gagné , Bravoo {joeur2} ")
        elif j2 > j1:
            os.system('color 2f')
            print(f"    {joeur1} est gagné , Bravoo {joeur1} ")
        else:
            print("    Match nul")
            os.system('color 40')
        input("")
        break
    else:
        if z % 2 == 0:
            print("    ", end="")
            print(joeur2, end="")
        else:
            print("    ", end="")
            print(joeur1, end="")

        n = input(", entrer un caractere : ")
        n = n.upper()
        os.system('cls')
        if n in mot:
            p = mot.index(n)  # la position de n sur le mot
            mot2[p] = n  # ajouter le caractere n sur le mot2(***********)
            mot[p] = "*"  # remplacer n par * sur le mot
            if z % 2 == 0:
                j1 += 1
                print("    ", end="")
                print("Bravo", joeur2)
            else:
                j2 += 1
                print("    ", end="")
                print("Bravo", joeur1)
        else:
            print("    ", end="")
            print("non existe ")

input()
