#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Chaine de responsabilité
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class Composant:
	def __init__(self, name, conditions):
		self.name = name
		self.conditions = conditions
		self.next = None
	def setNext(self, next):
		self.next = next
	def traitement(self, condition, message):
		if condition in self.conditions:
			print('Traitement du message %s par %s' % (message, self.name))
		if self.next is not None:
			self.next.traitement(condition, message)

c0 = Composant('c0', [1, 2])
c1 = Composant('c1', [1])
c2 = Composant('c2', [2])

c0.setNext(c1)
c1.setNext(c2)

c0.traitement(1, 'Test 1')
c0.traitement(2, 'Test 2')


