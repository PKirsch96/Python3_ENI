#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Memento
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class Current:
	def __init__(self, state):
		class Memento:
			state = None
		self.state = state
		self.memento = Memento()
	def setState(self, state):
		self.memento.state, self.state = self.state, state
	def resetState(self):
		state = self.memento.state
		if state is None:
			print("Il n'est pas possible d'aller en arrière")
		self.memento.state, self.state = None, self.memento.state

c = Current('1')
print(c.state)
c.setState('2')
print(c.state)
c.resetState()
print(c.state)
c.setState('3')
print(c.state)
c.resetState()
print(c.state)
c.resetState()

