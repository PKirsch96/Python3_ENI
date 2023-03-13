"""
Module regroupant toutes les fonctionnalités
permettant de demander une saisie dont la réponse est VRAI/OUI ou FAUX/NON
"""

OUI = ("o", "oui", "y", "yes", "1")
VRAI = ("v", "vrai", "t", "true", "1")


def demander_saisie_oui_ou_non(invite):
    """Par défaut, toute réponse non comprise vaut NON"""
    try:
        return input(invite).lower().replace(" ", "", 6) in OUI
    except Exception:
        return False


def demander_saisie_vrai_ou_faux(invite):
    """Par défaut, toute réponse non comprise vaut FAUX"""
    try:
        return input(invite).lower().replace(" ", "", 6) in VRAI
    except Exception:
        return False
