#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Adpatateur
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


class Chien:
	def aboyer(self):
		print('Ouaff')

class Chat:
	def miauler(self):
		print('Miaou')

class Cheval:
	def hennir(self):
		print('Hiiii')

class Cochon:
	def grogner(self):
		print('Gruik')


class Animal(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def faireDuBruit(self):
		return

class ChienAlternative(Animal, Chien):
	def faireDuBruit(self):
		return self.aboyer()

class ChatAlternative(Animal, Chat):
	faireDuBruit = Chat.miauler

class ChevalAlternative(Animal):
	def __init__(self, cheval):
		self.cheval = cheval
	def faireDuBruit(self):
		return self.cheval.hennir()
	def __getattr__(self, attr):
		return self.cheval.__getattr__(attr)

class CochonAdaptateur:
	def __init__(self, cochon):
		self.cochon = cochon
	def __getattr__(self, attr):
		if attr == 'faireDuBruit':
			return self.cochon.grogner
		return getattr(self.cochon, attr)

for animal in [ChienAlternative(), ChatAlternative(), ChevalAlternative(Cheval()), CochonAdaptateur(Cochon())]:
	animal.faireDuBruit()


class ChienAdaptateur:
	def __init__(self, chien):
		self.chien = chien
	def __getattr__(self, attr):
		if attr == 'faireDuBruit':
			return self.chien.aboyer
		return getattr(self.chien, attr)

class ChatAdaptateur:
	def __init__(self, chat):
		self.chat = chat
	def __getattr__(self, attr):
		if attr == 'faireDuBruit':
			return self.chat.miauler
		return getattr(self.chat, attr)

class ChevalAdaptateur:
	def __init__(self, cheval):
		self.cheval = cheval
	def __getattr__(self, attr):
		if attr == 'faireDuBruit':
			return self.cheval.hennir
		return getattr(self.cheval, attr)

def animal_adapterFactory(context):
	if isinstance(context, Chien):
		return ChienAdaptateur(context)
	elif isinstance(context, Chat):
		return ChatAdaptateur(context)
	elif isinstance(context, Cheval):
		return ChevalAdaptateur(context)
	elif isinstance(context, Cochon):
		return CochonAdaptateur(context)
	else:
		raise Exception('Adaptateur non trouvé')

for animal in [Chien(), Chat(), Cheval(), Cochon()]:
	animal_adapterFactory(animal).faireDuBruit()

