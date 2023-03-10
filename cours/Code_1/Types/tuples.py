#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Comparaisons basiques sur les performances des listes et n-uplets.
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Éditions ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from time import time

def test11():
	"""Utilisation de l'opérateur crochet (indice) pour la liste"""
	l = [1, 2, 3]
	for i in range(10000):
		l[1]

def test12():
	"""Utilisation de l'opérateur crochet (indice) pour le n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t[1]

def test21():
	"""Utilisation de l'opérateur crochet (tranche) pour la liste"""
	l = [1, 2, 3]
	for i in range(10000):
		l[:]

def test22():
	"""Utilisation de l'opérateur crochet (tranche) pour le n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t[:]

def test31():
	"""Utilisation de la méhode count pour la liste"""
	l = [1, 2, 3]
	for i in range(10000):
		l.count(2)

def test32():
	"""Utilisation de la méhode count pour le n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t.count(2)

def test41():
	"""Utilisation de la méhode index pour la liste"""
	l = [1, 2, 3]
	for i in range(10000):
		l.index(2)

def test42():
	"""Utilisation de la méhode index pour le n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t.index(2)

def test51():
	"""Utilisation de l'opérateur in pour la liste"""
	l = [1, 2, 3]
	for i in range(10000):
		2 in l

def test52():
	"""Utilisation de l'opérateur in pour le n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		2 in t

def test61():
	"""Utilisation de l'opérateur + pour la liste"""
	l = [1, 2, 3]
	for i in range(10000):
		l + [4, 5, 6]

def test62():
	"""Utilisation de l'opérateur + pour le n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t + (4, 5, 6)

def test71():
	"""Utilisation de l'opérateur * pour la liste"""
	l = [1, 2, 3]
	for i in range(10000):
		l * 5

def test72():
	"""Utilisation de l'opérateur * pour le n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t * 5

if __name__ == "__main__":
	t0 = time()
	test11()
	t1 = time()
	test12()
	t2 = time()

	print('> crochet')
	print('listes : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test21()
	t1 = time()
	test22()
	t2 = time()

	print('> slice')
	print('listes : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test31()
	t1 = time()
	test32()
	t2 = time()

	print('> count')
	print('listes : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test41()
	t1 = time()
	test42()
	t2 = time()

	print('> index')
	print('listes : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test51()
	t1 = time()
	test52()
	t2 = time()

	print('> in')
	print('listes : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test61()
	t1 = time()
	test62()
	t2 = time()

	print('> +')
	print('listes : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test71()
	t1 = time()
	test72()
	t2 = time()

	print('> *')
	print('listes : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

