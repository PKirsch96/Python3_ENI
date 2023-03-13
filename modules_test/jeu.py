
from saisie import (
    demander_saisie_nombre_borne,
    demander_saisie_oui_ou_non,
    menu,
)


def jouer_un_coup(nombre, minimum, maximum, aide):
    essai = demander_saisie_nombre_borne("Devinez le nombre", minimum, maximum)

    # On teste si l'essai est correct ou non
    if essai < nombre or essai < minimum:
        print("Trop petit")
        if aide:
            minimum = essai + 1
        victoire = False
    elif essai > nombre or essai > maximum:
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


def jouer_une_partie(nombre, minimum, maximum, aide, nb_coups):

    coups = 0
    gagnants = {}

    while True:
        # On entre dans une boucle infinie
        # qui permet de jouer plusieurs coups

        victoire, minimum, maximum = jouer_un_coup(nombre,
                                                   minimum, maximum, aide)

        coups += 1

        if coups == int(nb_coups):
            print("défaite !")

            tableau_gagnants = dict(sorted(
                gagnants.items(), key=lambda item: item[1]))

            return tableau_gagnants

        elif (victoire):
            prenom = input(
                "quel est votre prénom ? : "
                ).lower().replace(" ", "", 6)

            gagnants[prenom] = coups

            tableau_gagnants = dict(sorted(
                gagnants.items(), key=lambda item: item[1]))

            return tableau_gagnants


def choix_du_joueur():

    level, aide = menu()
    # tableau pour définir le nombre max
    lvl = (100, 1000, 1000000, 1000000000000)
    # nombres de coups autorisé en fonction du niveau choisi
    nb_coups_lvl = (9, 20, 40, 60)

    while True:

        minimum = 0

        maximum = lvl[(int(level)-1)]

        nb_coups = nb_coups_lvl[(int(level)-1)]

        if maximum > minimum:

            return minimum, maximum, aide, nb_coups


def jouer():
    tableau_gagnants = {}
    minimum, maximum, aide, nb_coups = choix_du_joueur()
    while True:

        nombre = demander_saisie_du_nombre_mystere(minimum, maximum)

        gagnants = jouer_une_partie(nombre, minimum, maximum, aide, nb_coups)

        tableau_gagnants.update(gagnants)

        print(tableau_gagnants)

        if not demander_saisie_oui_ou_non(
            "Souhaitez-vous refaire une nouvelle partie ? : "
        ):
            print("A bientôt !")
            return

        elif demander_saisie_oui_ou_non("changer de niveau ? : "):
            minimum, maximum, aide, nb_coups = choix_du_joueur()
