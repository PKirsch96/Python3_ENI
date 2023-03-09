import random


def demander_saisie_nombre(invite, minimum, maximum):
    invite += f"entre {minimum} et {maximum} : "
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
#nombre = random.randint(0,100)
nombre = demander_saisie_nombre(f"Saisissez le nombre à deviner", 0, 50)

print("\n\nEssayer de devinner le nombre de l'ordinateur\n\n") 
while True:
    joueur  = demander_saisie_nombre(f"Saisissez un nombre", 0, 50) 
    if nombre > joueur:
        print("plus grand")
    elif nombre < joueur:
        print("plus petit")
    else:
        print(f"\nbravo c'était bien {joueur}")
        break
       

