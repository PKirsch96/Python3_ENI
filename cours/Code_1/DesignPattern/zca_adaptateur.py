#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Adaptateur utilisant la ZCA
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implements
from zope.component import adapts


class IChien(Interface):
	nom = Attribute("""Nom du chien""")
	def aboyer(filename):
		"""Méthode permettant de le faire aboyer"""

class Chien(object):
	implements(IChien)
	nom = u''
	def __init__(self, nom):
		self.nom = nom
	def aboyer(self):
		"""Méthode permettant de le faire aboyer"""
		print('Ouaff')

class IChat(Interface):
	nom = Attribute("""Nom du chat""")
	def miauler(filename):
		"""Méthode permettant de le faire miauler"""

class Chat(object):
	implements(IChien)
	nom = u''
	def __init__(self, nom):
		self.nom = nom
	def miauler(self):
		"""Méthode permettant de le faire miauler"""
		print('Miaou')

class IAnimal(Interface):
	def exprimer(self):
		"""Methode permettant à un animal de s'exprimer"""

class Animal(object):
	implements(IAnimal)
	adapts(Chien, Chat)
	def __init__(self, animal):
		self.animal = animal
	def exprimer(self):
		"""Methode permettant à un animal de s'exprimer"""
		if isinstance(self.animal, Chien):
			self.animal.aboyer()
		elif isinstance(self.animal, Chat):
			self.animal.miauler()
		else:
			raise Exception("Cet animal ne sait pas s'exprimer")

bambou = Chien('Bambou')
Animal(bambou).exprimer()

