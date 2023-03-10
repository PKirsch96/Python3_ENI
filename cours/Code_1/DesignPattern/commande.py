#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Commande
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"



import abc


class Mobile:
	def deplacerGauche(self):
		print('Le mobile se déplace à gauche')
	def deplacerDroite(self):
		print('Le mobile se déplace à droite')

class Commande(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def executer(self):
		return

class GaucheCommande(Commande):
	def __init__(self, mobile):
		self.mobile = mobile
	def executer(self):
		self.mobile.deplacerGauche()

class DroiteCommande(Commande):
	def __init__(self, mobile):
		self.mobile = mobile
	def executer(self):
		self.mobile.deplacerDroite()

class Pilote:
	def __init__(self, cG, cD):
		self.commandeGauche = cG
		self.commandeDroite = cD
	def ordreGauche(self):
		self.commandeGauche.executer()
	def ordreDroite(self):
		self.commandeDroite.executer()

mobile = Mobile()
commande_gauche = GaucheCommande(mobile)
commande_droite = DroiteCommande(mobile)
pilote = Pilote(commande_gauche, commande_droite)

pilote.ordreGauche()
pilote.ordreDroite()

