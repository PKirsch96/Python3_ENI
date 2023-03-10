#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Définition d'une liste d'entiers et quelques tests unitaires.
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import unittest


class numberlist(list):
	"""Liste de nombres"""

	__types__ = [type(0), type(0.)]

	def __init__(self, seq=[]):
		"""Surcharge générique du constructeur"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("l'objet %s d'index %s de la séquence n'est pas un nombre" % (value, index))
		list.__init__(self, seq)

	def append(self, value):
		"""Surcharge de la méthode d'ajout d'éléments en fin de liste"""
		if type(value) not in self.__types__:
			raise TypeError("%s n'est pas un nombre" % value)
		list.append(self, value)

	def insert(self, index, value):
		"""Surcharge de la méthode d'ajout d'éléments à un index donné"""
		if type(value) not in self.__types__:
			raise TypeError("%s n'est pas un nombre" % value)
		list.insert(self, index, value)

	def extend(self, seq):
		"""surcharge de la méthode de modification de plusieurs éléments"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("l'objet %s d'index %s de la séquence n'est pas un nombre" % (value, index))
		list.extend(self, seq)

	def __setitem__(self, index, value):
		"""Surcharge de la méthode de modification d'un élément"""
		if type(value) not in self.__types__:
			raise TypeError("%s n'est pas un nombre" % value)
		list.__setitem__(self, index, value)

	def __setslice__(self, i, j, seq):
		"""surcharge de la méthode de modification de plusieurs éléments"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("l'objet %s d'index %s de la séquence n'est pas un nombre" % (value, index))
		list.__setslice__(self, i, j, seq)

	def __add__(self, seq):
		"""surcharge de la méthode d'ajout de plusieurs éléments"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("l'objet %s d'index %s de la séquence n'est pas un nombre" % (value, index))
		return list.__add__(self, seq)

	def __iadd__(self, seq):
		"""surcharge de la méthode d'ajout de plusieurs éléments"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("l'objet %s d'index %s de la séquence n'est pas un nombre" % (value, index))
		list.__iadd__(self, seq)
		return self

class numberlistTest(unittest.TestCase):
	"""Test des listes de nombres"""

	def testConstuct(self):
		self.test = numberlist([1, 2.])
		self.assertEqual(self.test, [1, 2.])
		self.assertRaises(TypeError, numberlist, ['7'])

	def testAppend(self):
		self.test = numberlist()
		self.test.append(5)
		self.assertEqual(self.test, [5])
		self.test.append(6.)
		self.assertEqual(self.test, [5, 6.])
		self.assertRaises(TypeError, self.test.append, '7')

	def testInsert(self):
		self.test = numberlist()
		self.test.insert(0, 5)
		self.assertEqual(self.test, [5])
		self.test.insert(1, 6.)
		self.assertEqual(self.test, [5, 6.])
		self.assertRaises(TypeError, self.test.append, '7')

	def testExtend(self):
		self.test = numberlist()
		self.test.extend([5, 7, 9.])
		self.assertEqual(self.test, [5, 7, 9.])
		self.assertRaises(TypeError, self.test.extend, [5, '7', 9.])
		self.assertEqual(self.test, [5, 7, 9.])

	def testSetitem(self):
		self.test = numberlist([5])
		self.assertEqual(self.test, [5])
		self.test[0] = 1
		self.assertEqual(self.test, [1])
		self.assertRaises(TypeError, self.test.__setitem__, 0, '7')

	def testSetslice(self):
		self.test = numberlist([1, 2, 3])
		self.assertEqual(self.test, [1, 2, 3])
		self.test[:2] = [0] *2
		self.assertEqual(self.test, [0, 0, 3])
		self.assertRaises(TypeError, self.test.__setslice__, 0, 2, [1, '7'])

	def testAdd(self):
		self.test = numberlist()
		test = self.test + [5, 7, 9.]
		self.assertEqual(test, [5, 7, 9.])
		self.assertRaises(TypeError, self.test.__add__, [5, '7', 9.])
		self.assertEqual(self.test, [])

	def testIadd(self):
		self.test = numberlist()
		self.test += [5, 7, 9.]
		self.assertEqual(self.test, [5, 7, 9.])
		self.assertRaises(TypeError, self.test.__iadd__, [5, '7', 9.])
		self.assertEqual(self.test, [5, 7, 9.])

if __name__ == "__main__":
	unittest.main()

