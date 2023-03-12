import sys

MIN = 0
MAX = 99


def demander_saisie_nombre(invite):
    while True:

        print(invite, end=": ")
        saisie = input()

        try:
            saisie = int(saisie)
        except:
            print("Seul les caractères [0-9] sont autorisés.", file=sys.stderr)
        else:

            return saisie


def demander_saisie_nombre_borne(invite, minimum=MIN, maximum=MAX):
    while True:

        invite = "{} entre {} et {} inclus".format(invite, minimum, maximum)
        saisie = demander_saisie_nombre(invite)

        if minimum <= saisie <= maximum:
            return saisie


def jouer_un_coup(nombre, minimum, maximum):
    essai = demander_saisie_nombre_borne("Devinez le nombre", minimum, maximum)

    if essai < nombre:
        print("Trop petit")
        minimum = essai + 1
        victoire = False
    elif essai > nombre:
        print("Trop grand")
        maximum = essai - 1
        victoire = False
    else:
        print("Gagné!")
        victoire = True
        minimum = maximum = essai
    return victoire, minimum, maximum


def decider_bornes():
    while True:
        minimum = demander_saisie_nombre("Quelle est la borne minimale ?")
        maximum = demander_saisie_nombre("Quelle est la borne maximale ?")
        if maximum > minimum:
            return minimum, maximum


def demander_saisie_du_nombre_mystere(minimum, maximum):
    return demander_saisie_nombre_borne("Saisissez le nombre à deviner",
                                        minimum, maximum)


def jouer_une_partie(nombre, minimum, maximum):
    while True:

        victoire, minimum, maximum = jouer_un_coup(nombre, minimum, maximum)

        if (victoire):
            return


def jouer():
    minimum, maximum = decider_bornes()
    nombre = demander_saisie_du_nombre_mystere(minimum, maximum)
    jouer_une_partie(nombre, minimum, maximum)


if __name__ == '__main__':
    print("Le module est exécuté")
    jouer()
else:
    print("Le module a été importé")
