#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Patron de conception Rappel
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"

def callback():
	print('Fonction de rappel')

def do(value, *args, callback):
	print('Action')
	if value > 0:
		callback()

do(0, callback=callback)
do(1, callback=callback)

class A:
	def __init__(self, name):
		self.name = name
	def do(self, *args, callback):
		callback(self.name)

class B:
	def print(self, name):
		print(name)

a = A('Test')
a.do(callback=B().print)

