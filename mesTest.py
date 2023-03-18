from itertools import cycle
from itertools import product
from itertools import chain
import math

from random import choice, sample

tableau = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"],
           [1, 2, 3, 4, 5, 6, 4, 8, 7, 9, 5, 2, 1, 4, 7, 4, 1]]

# for case in chain.from_iterable(tableau):
#     print(case)
# instade of
# for ligne in tableau:
#     for case in ligne:
#         print(case)
# for j, colonne in enumerate(tableau):
#     for i, case in enumerate(colonne):
#         print(f"tableau[{i}][{j}] = {case}")

# transpose = zip(*tableau).__str__()
# print(transpose)
# print(tableau)


# lignes = ["A", "B", "C"]
# colonnes = [1, 2, 3]


# for ligne, colonne in product(lignes, colonnes):
#     print(f"Case {ligne}{colonne}")


# for numero, lettre in zip(range(10), cycle("ABC")):
#     print("Case {}{}".format(lettre, numero))

# def my_decorator(func):
#     def wrapper():
#         num = int(func())
#         return num * 2
#     return wrapper


# @my_decorator
# def number():
#     return 123


# print(number())
carnet = {
    "Clément": "0601020304",
    "Chloé": "0102030405",
    "Matthieu": "0205080502",
}

carnet["Sébastien"] = "0408060204"

# for nom, telephone in carnet.items():
#     print(f"Le numéro de {nom} est {telephone}")

# for nom in sorted(carnet.keys()):
#     print(f"Le numéro de {nom} est {carnet[nom]}")

# print("Cassiopée" in carnet)
#
#
# lol = carnet.get("Cassiopée", "0987654321")
# print(lol)
#
# cartes = {
#     chr(0x1f0a1): 11,
#     chr(0x1f0a2): 2,
#     chr(0x1f0a3): 3,
#     chr(0x1f0a4): 4,
#     chr(0x1f0a5): 5,
#     chr(0x1f0a6): 6,
#     chr(0x1f0a7): 7,
#     chr(0x1f0a8): 8,
#     chr(0x1f0a9): 9,
#     chr(0x1f0aa): 10,
#     chr(0x1f0ab): 10,
#     chr(0x1f0ad): 10,
#     chr(0x1f0ae): 10,
# }
#
# liste_cartes = list(cartes)
#
# carte = choice(liste_cartes)
# score = cartes[carte]
# print(carte)
# print(score)
# print("------------------------------------------------------------")
#
# carte = choice(liste_cartes)
# score += cartes[carte]
# print(carte)
# print(score)
# print("------------------------------------------------------------")
# main_banque = sample(liste_cartes, 2)
# score_banque = sum(cartes[carte] for carte in main_banque)
#
# print(main_banque)
# print(score_banque)

# print("je rajoute un bout de phrase | ", end=" ")
# print("avec un autre print grâce à : end=\" \"")


class Point:
    """Représente un point dans l'espace"""

    def __init__(self, x, y, z):
        """Méthode d'initialisation d'un point dans l'espace"""
        self.x, self.y, self.z = x, y, z

    def distance(self, other=None):
        """Renvoi la distance par rapport à un autre point ou par défaut à l'origine"""
        if other is None:
            other = Point(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        """Opérateur de soustraction"""
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other):
        """Opérateur de multiplication"""
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self

    def __str__(self):
        """Représentation d'un point souiuis la forme d'une chaîne de caractère"""
        return "Point ({self.x}, {self.y}, {self.z})".format(self=self)


p = Point(1, 2, 3)
lol = Point(2, 3, 4)
p *= lol
print(p)

print("Mise en évidence d'un problèujyme d'optimisation")
print(id(p))

print(id(p))
print(p)


