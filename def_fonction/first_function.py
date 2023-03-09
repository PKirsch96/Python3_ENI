import random
def demander_saisie_nombre():
    while True:
        saisie = input("Saisissez un nombre entre 0 et 99 : ")
        try:
            saisie = int(saisie)
        except:
            pass
        else:
            if 9 <= saisie <= 99:
                break
    return saisie

print("saisissez le numéro à devinner")
nombre = random.randint(0,100)

print("Essayer de devinner votre propre chiffre")