"""liste=[1,3,8,6,12,78,15,4,69,13]
listepaire=[]
listeimpaire=[]
for i in liste:
    if i%2==0:
        listepaire.append(i)
    else:
        listeimpaire.append(i)
print(listepaire)
print(listeimpaire)"""


def equation(x):
    return 2*x**3 + 5*x**2 +5*x +3
x=int(input("enter x"))
print("nous avons  ",equation(x))
#print("nous avons ",equation(2)) #2*x**3
