
from saisie import (
    demander_saisie_nombre,
    demander_saisie_nombre_borne,
    demander_saisie_oui_ou_non,
    menu,
)


def jouer_un_coup(nombre, minimum, maximum, aide):
    essai = demander_saisie_nombre_borne("Devinez le nombre", minimum,
                                         maximum)

    # On teste si l'essai est correct ou non
    if essai < nombre:
        print("Trop petit")
        if aide:
            minimum = essai + 1
        victoire = False
    elif essai > nombre:
        print("Trop grand")
        if aide:
            maximum = essai - 1
        victoire = False
    else:
        print("Gagné!")
        victoire = True
        minimum = maximum = essai
    return victoire, minimum, maximum


def demander_saisie_du_nombre_mystere(minimum, maximum):
    return demander_saisie_nombre_borne("Saisissez le nombre à deviner",
                                        minimum, maximum)


def jouer_une_partie(nombre, minimum, maximum, aide):
    while True:
        # On entre dans une boucle infinie
        # qui permet de jouer plusieurs coups

        victoire, minimum, maximum = jouer_un_coup(nombre,
                                                   minimum, maximum, aide)

        if (victoire):
            return


def choix_du_joueur():
    level, aide = menu()
    choix = int(level)
    niveaux = (100, 1000, 1000000, 1000000000000)
    while True:
        minimum = 0
        if choix == 1:
            maximum = niveaux[0]
        if choix == 2:
            maximum = niveaux[1]
        if choix == 3:
            maximum = niveaux[2]
        if choix == 4:
            maximum = niveaux[3]

        if maximum > minimum:
            return minimum, maximum, aide


def jouer():
    minimum, maximum, aide = choix_du_joueur()
    while True:
        nombre = demander_saisie_du_nombre_mystere(minimum, maximum)
        jouer_une_partie(nombre, minimum, maximum, aide)
        if not demander_saisie_oui_ou_non("Souhaitez-vous refaire une nouvelle partie ?"):
            print("A bientôt !")
            return
        elif demander_saisie_oui_ou_non("changer de niveau ? : "):
            minimum, maximum, aide = choix_du_joueur()
