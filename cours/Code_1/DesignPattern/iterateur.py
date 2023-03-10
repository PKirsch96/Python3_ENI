#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Iterateur
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

class Iterateur:
	def __init__(self, context):
		self.context = context.childs()
	def __iter__(self):
		return self
	def __next__(self):
		if len(self.context) == 0:
			raise StopIteration
		return self.context.pop(0)

class Composant(metaclass=abc.ABCMeta):
	def __init__(self, name):
		self.name = name
	@abc.abstractmethod
	def verbose(self, level=0):
		return
	def __iter__(self):
		return Iterateur(self)

class Feuille(Composant):
	def verbose(self, level=0):
		return '%sFeuille %s' % ('\t' * level, self.name)
	def childs(self):
		return [self]

class Composite(Composant):
	def __init__(self, name):
		Composant.__init__(self, name)
		self.contenu = []
	def add(self, composant):
		self.contenu.append(composant)
	def verbose(self, level=0):
		feuilles = [f.verbose(level+1) for f in self.contenu]
		feuilles.insert(0, '%sComposite %s' % ('\t' * level, self.name))
		return '\n'.join(feuilles)
	def childs(self):
		result = [self]
		for f in self.contenu:
			result.extend(f.childs())
		return result

c1 = Feuille('F1')
c2 = Feuille('F2')
c3 = Composite('C1')
c3.add(Feuille('F4'))
c3.add(Feuille('F5'))
c3.add(Feuille('F6'))
c4 = Composite('C2')
c41 = Composite('C3')
c41.contenu = [Feuille('F7'), Feuille('F8'), Feuille('F9')]
c4.contenu = [Composite('C4'), c41, Feuille('FA')]

main = Composite('Test')
main.contenu.extend([c1, c2, c3, c4])

print(main.verbose())


for a in main:
	print(a.name)

