import numpy
from numpy import *
from fractions import *
import Bezout


def modular_inverse(m):
	"""Finds the inverse of a matrix (modulo 26)"""

	mat = matrix(m)
	inv_matrix = mat.I
	determinant = int(round(numpy.linalg.det(mat)))
	mvint = inv_matrix*determinant
	(u,v,g) = Bezout.bezout(determinant,26)
	inv_determinant = u
	inv_matrix = (inv_determinant * mvint)%26

	return inv_matrix