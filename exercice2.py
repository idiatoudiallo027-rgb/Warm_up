def PoidIdeal(taille,sexe):
    sexe=sexe.upper()
    if sexe=="M":
        return  taille-100- (taille -150) /4
    elif sexe=="F":
        return  taille-100- (taille -150) /2.5
    else:
        print("no found")
print("le poid idiale est",PoidIdeal(150,"m"))
print("le poid idiale est",PoidIdeal(110,"f"))
print("le poid idiale est",PoidIdeal(1





45,"m"))
