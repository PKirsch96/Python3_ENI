import random


MIN = 0
MAX = 100

def demander_saisie_nombre(invite):
    invite += f"entre {MIN} et {MAX} : "
    while True:
        saisie = input(invite)
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
joueur  = demander_saisie_nombre(f"Saisissez un nombre") 
while nombre != joueur:
    joueur
    if nombre > joueur:
        print("plus grand")
    else:
        print("plus petit")
    joueur  = demander_saisie_nombre(f"Saisissez un nombre") 
       
print(f"\nbravo c'était bien {joueur}")
