import string,random,os
from os import system
os.system('cls')
print("     1- light mode :")
print("     2- Dark mode :")
mode=int(input("     1/2 ? :"))
if mode==1:
    os.system('color F0')
else:
    os.system('color 0F')
os.system('cls')
S = random.randint(4,9)  #nombre de caractère aléatoire 
m = ''.join(random.choices(string.ascii_uppercase ,k = S)) #random string 
#m='PYTHON'
mot=[]
for i in m:     
    mot.append(i)
mot3=[]
for i in m:
    mot3.append(i)
mot2=[] #ajouter une liste des etoiles
for i in range(len(mot)):
    mot2.append("*")
print("     Essayez de découvrir le mot de passe suivant :")
#print(strmot2)
essei=0
while True:
    print()
    print("       ",end="")
    print(" ".join(mot2)) #ListeToString
    essei+=1
    MaxEssai=len(m)*6
    if essei==MaxEssai and mot2 != mot3: #verifier le nombre d'essais
        os.system('color 4F')
        print("     vous avez d'eppaser le nombre d'essais !",)
        break
    elif mot2==mot3 :  #si le mot est complet
        os.system('color AF')
        print("     Bravo, vous avez gagné")
        break
    else:
        n=input("     entrer un caractère : ")
        n=n.upper()
        os.system('cls')
        if n in mot:
            p=mot.index(n)       #la position de n sur le mot
            mot2[p]=n            #ajouter le caractere n sur le mot2(***********)
            mot[p]="*"           #remplacer n par * sur le mot 
            print(f"     vous reste {MaxEssai-essei-1} essais.")
        else:
            if MaxEssai-essei-1 >0: 
                print(f"     vous reste {MaxEssai-essei-1} essais.")
input("")