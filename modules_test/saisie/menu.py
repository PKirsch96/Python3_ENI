from .booleen import (
    demander_saisie_oui_ou_non
)
import sys

LEVEL = (1, 2, 3, 4)


def menu():
    while True:
        level = input(
            "Bonjour choisissez un niveau de difficulté de 1 à 4 : "
            )
        aide = demander_saisie_oui_ou_non("voulez vous activez l'aide ? :")

        try:
            int(level) in LEVEL
        except Exception:
            print("Seul les caractères [1-4] sont autorisés.", file=sys.stderr)
        else:
            return level, aide
