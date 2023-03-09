import random
def demander_saisie_nombre():
    while True:
        saisie = input("Saisissez un nombre entre 0 et 99 : ")
        try:
            saisie = int(saisie)
        except:
            pass
        else:
            if 0 <= saisie <= 99:
                break
    return saisie

print("\nl'ordinateur choisi le nombre à devinner\n\n")
nombre = random.randint(0,100)

print("Essayer de devinner le nombre de l'ordinateur")
joueur  = demander_saisie_nombre() 
while nombre != joueur:
    joueur
    if nombre > joueur:
        print("plus grand")
    else:
        print("plus petit")
    joueur  = demander_saisie_nombre() 
       
print(f"\nbravo c'était bien {joueur}")
