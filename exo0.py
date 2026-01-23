liste=[]
while True:
    nombre=int(input("entrer un nombre positif:"))
    if nombre <=0:
        break
    else:
        liste.append(nombre)
maximum=liste[0]
minimum=liste[0]
for i in liste:
    if i> maximum:
        maximum=i
    if i<minimum:
        minimum=i
print(liste)
print(f"le minimum de la liste est {minimum}")
print(f"le maximum de la liste est {maximum}")

