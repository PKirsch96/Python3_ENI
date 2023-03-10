#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Observateur
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"

class Event:
	def __init__(self, name):
		self.name = name

class Observable:
	def __init__(self):
		self.observers = set()
	def addObserver(self, observer):
		self.observers.add(observer)
	def removeObserver(self, observer):
		self.observers.remove(observer)
	def notify(self, datas):
		for o in self.observers:
			o.update(datas)

class Observer:
	def __init__(self, name):
		self.name = name
		self.listeners = []
	def update(self, datas):
		print('Mise à jour de %s avec %s' % (self.name, datas))

observable = Observable()
observer1 = Observer('Observer 1')
observable.addObserver(observer1)
observer2 = Observer('Observer 2')
observable.addObserver(observer2)

observable.notify('Des données')
observable.notify('Encore plus de données')

