# import random
import sys


MIN = 0
MAX = 99


def demander_saisie_nombre(invite):
    while True:
        saisie = input(invite + ": ")
        try:
            saisie = int(saisie)
        except Exception:
            print("Seul les caractères [0-9] sont autorisés.", file=sys.stderr)
        else:
            return saisie


def demander_saisie_nombre_borne(invite, minimum=MIN, maximum=MAX):
    invite = f"{invite} entre {minimum} et {maximum} inclus"
    while True:
        saisie = demander_saisie_nombre(invite)
        if minimum <= saisie <= maximum:
            return saisie


def jouer_un_coup(nombre, minimum, maximum):

    joueur = demander_saisie_nombre_borne(
        "Saisissez un nombre", minimum, maximum)

    if nombre > joueur:
        print("plus grand")
        minimum = joueur + 1
        victoire = False
    elif nombre < joueur:
        print("plus petit")
        maximum = joueur - 1
        victoire = False
    else:
        print(f"\nbravo c'était bien {joueur}")
        victoire = True
        minimum = maximum = joueur
    return victoire, minimum, maximum


def jouer_une_partie(nombre, minimum, maximum):
    victoire = False
    while not victoire:
        victoire, minimum, maximum = jouer_un_coup(
            nombre,
            minimum,
            maximum,
        )


def demander_saisie_du_nombre_mystere(minimum, maximum):
    return demander_saisie_nombre_borne(
        "Saisissez le nombre à deviner",
        minimum,
        maximum,
    )


def decider_bornes():
    while True:
        minimum = demander_saisie_nombre(
            "Quelle est la borne minimale ?")
        maximum = demander_saisie_nombre(
            "Quelle est la borne maximale ?"
        )
        if maximum > minimum:
            return minimum, maximum


def jouer():
    minimum, maximum = decider_bornes()
    nombre = demander_saisie_du_nombre_mystere(minimum, maximum)
    jouer_une_partie(nombre, minimum, maximum)


jouer()
