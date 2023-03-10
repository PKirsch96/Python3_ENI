#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Monteur
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


class Produit:
	@property
	def forme(self):
		return self._forme
	@forme.setter
	def forme(self, forme):
		self._forme = forme
	@property
	def couleur(self):
		return self._couleur
	@couleur.setter
	def couleur(self, couleur):
		self._couleur = couleur
	def __str__(self):
		return 'Produit forme=%s couleur=%s' % (self.forme, self.couleur)

class Monteur:
	@property
	def produit(self):
		return self._produit
	@produit.setter
	def produit(self, produit):
		self._produit = produit
	def creerProduit(self):
		self.produit = Produit()
	@abc.abstractmethod
	def concevoirForme(self):
		return
	@abc.abstractmethod
	def concevoirCouleur(self):
		return

class MonteurCubeBleu(Monteur):
	def concevoirForme(self):
		self.produit.forme = "Cube"
	def concevoirCouleur(self):
		self.produit.couleur = "Bleu"

class MonteurSphereRouge(Monteur):
	def concevoirForme(self):
		self.produit.forme = "Sphere"
	def concevoirCouleur(self):
		self.produit.couleur = "Rouge"

class MonteurPyramideJaune(Monteur):
	def concevoirForme(self):
		self.produit.forme = "Pyramide"
	def concevoirCouleur(self):
		self.produit.couleur = "Jaune"

class Directeur:
	@property
	def monteur(self):
		return self._monteur
	@monteur.setter
	def monteur(self, monteur):
		self._monteur = monteur
	def concevoirProduit(self):
		self.monteur.creerProduit()
		self.monteur.concevoirForme()
		self.monteur.concevoirCouleur()
		return self.monteur.produit

directeur = Directeur()
directeur.monteur = MonteurPyramideJaune()
produit = directeur.concevoirProduit()
print(produit)

