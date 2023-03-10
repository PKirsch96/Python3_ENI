#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Prototype
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


class A:
	pass

class NonPrototype:
	def __init__(self):
		# Méthode complexe de création
		self.a = 42
		self.b = 'Complexe'
		self.c = A()
		self.c.a = [1, 2, 3]
		self.c.b = A()
		self.c.b.a = (1, 2, 3)
	def __str__(self):
		return 'Prototype {self.a}, {self.b}, {self.c.a}, {self.c.b.a}'.format(self=self)

a = NonPrototype()
print(a)

from copy import deepcopy
class Prototype:
	_instance_reference = None
	def __new__(cls):
		if cls._instance_reference is not None:
			print('Clonage')
			result = object.__new__(cls)
			result.__dict__ = deepcopy(cls._instance_reference.__dict__)
			return result
		result = object.__new__(cls)
		cls._instance_reference = result
		return result
	def __init__(self):
		if self._instance_reference is None:
			return
		self._instance_reference = None
		print('Initialisation')
		# Méthode complexe de création
		self.a = 42
		self.b = 'Complexe'
		self.c = A()
		self.c.a = [1, 2, 3]
		self.c.b = A()
		self.c.b.a = (1, 2, 3)
	def __str__(self):
		return '{self.__class__.__name__} {0}, {self.a}, {self.b}, {self.c.a}, {self.c.b.a}'.format(id(self), self=self)

print(Prototype._instance_reference)
b = Prototype()
print(b)
print(Prototype._instance_reference, b._instance_reference)
c = Prototype()
print(c)
print(Prototype._instance_reference, c._instance_reference)

