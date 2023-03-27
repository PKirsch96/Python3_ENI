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
#
#
# class AffichableMixin:
#
#     str_format = "PrettyPrintableObject"
#
#     def __str__(self) -> str:
#         return self.str_format.format(self=self)
#
#
# class NomAutomatiqueMixin:
#
#     ordinal = 65
#
#     def __init__(self) -> None:
#         self.lettre = chr(NomAutomatiqueMixin.ordinal)
#         NomAutomatiqueMixin.ordinal += 1
#
#
# class Point(AffichableMixin, NomAutomatiqueMixin):
#     """Représente un point dans l'espace"""
#
#     str_format = "Point {self.lettre} ({self.x}, {self.y}, {self.z})"
#
#     def __init__(self, x, y, z):
#         """Méthode d'initialisation d'un point dans l'espace"""
#         super().__init__()
#         self.x, self.y, self.z = x, y, z
#
#     def distance(self, other=None):
#         """Renvoi la distance par rapport à un autre
#         point ou par défaut à l'origine"""
#         if other is None:
#             other = Point(0, 0, 0)
#         return ((self.x-other.x)**2 + (self.y-other.y)**2
#                 + (self.z-other.z)**2) ** (1 / 2)
#
#     def __iadd__(self, other):
#         self.x += other.x
#         self.y += other.y
#         self.z += other.z
#         return self
#
#     def __sub__(self, other):
#         """Opérateur de soustraction"""
#         self.x -= other.x
#         self.y -= other.y
#         self.z -= other.z
#         return self
#
#     def __mul__(self, other):
#         """Opérateur de multiplication"""
#         self.x *= other.x
#         self.y *= other.y
#         self.z *= other.z
#         return self
#
#
# class Point2D(Point):
#
#     str_format = "Point2D {self.lettre} ({self.x}, {self.y})"
#
#     def __init__(self, x, y):
#         super().__init__(x, y, 0)
#
#
# p = Point(1, 2, 3)
# print(p)
# p = Point2D(3, 4)
# print(p)


# # class Test:
# #     def __init__(self, chiffre):
# #         self.chiffre = chiffre

#     def __sub__(self, other):
#         return self.chiffre - other

#     def __neg__(self):
#         return - self.chiffre


# lol = Test(25)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# # if (n := len(a)) > 10:
##      print(f"list is too long({n} elements, expected <=10)")


# # str = "1234"

# print(list(str))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# if (n := len(a)) > 10:
#     print(f"list is too long({n} elements, expected <=10)")


# str = "1234"

# print(list(str))
# # def f(x): return x**2


# lolilol = list(filter(lambda x: x < 81, map(lambda x: x**2, range(10))))

# print(lolilol)

# for n in range(2, 10):

#     print("n = ", n)

#     x = 2

#     print("x = ", x)

#     while x < n ** (1/2):

#         if n % x == 0:

#             print('%i vaut %i * %i' % (n, x, n/x))

#             break

#         print("x = ", x)

#         x += 1

#         print("x = ", x)

#     else:

#         print('%i est un nombre premier' % n)

#     n += 1

# def g():
#     yield 1
#     yield 2
#     yield 3


# gen = g()
# def f():
#     a = 1
#     while True:
#         a *= 2
#         if a > 1_000_000:
#             break
#     return a


# print(next(gen))
# print(next(gen))
# print(next(gen))
# def positive(lol):
#     for a in lol:
#         if a < 0:
#             continue
#         print(a)


# positive([1, -5, 25, -47, 5, -5, -7, -9, 2])

# liste = [a**2 for a in range(10)]

# print(liste)

# # with open('exemple.txt') as fichier:
# #     content = fichier.read()
# #     print(content)

# a: int() = "lol"

# print(type(a))

numbers = [1, 2, 3, 4, 5]
print(numbers[-1:-6:-2])