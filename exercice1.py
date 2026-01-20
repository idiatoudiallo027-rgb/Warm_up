liste=[]
while True:
    n=int(input("entrer un nombre positif:"))
    if n<=0:
        break
    liste.append(n)
#affichage
print(liste)
print("la plus grand valeur est",max(liste))
print("la plus petite valeur est", min(liste))




