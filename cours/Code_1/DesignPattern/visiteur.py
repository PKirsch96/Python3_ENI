#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Visiteur
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class Visiteur1:
	def visiterCarre(self, carre):
		print('Visite du carré')
	def visiterCercle(self, cercle):
		print('Visite du cercle')

class Visiteur2:
	def visiterCarre(self, carre):
		print(carre.mesure)
	def visiterCercle(self, cercle):
		print(cercle.mesure)

class Carre:
	mesure = 'longueur du coté'
	def accept(self, visiteur):
		visiteur.visiterCarre(self)

class Cercle:
	mesure = 'rayon'
	def accept(self, visiteur):
		visiteur.visiterCercle(self)

Carre().accept(Visiteur1())
Cercle().accept(Visiteur2())

