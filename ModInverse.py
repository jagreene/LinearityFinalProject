import numpy
from numpy import *
from fractions import *
import Bezout

def modular_inverse(m):
	mat = matrix(m)

	inv_matrix = mat.I

	determinant = int(round(numpy.linalg.det(mat)))

	mvint = inv_matrix*determinant
	
	(u,v,g) = Bezout.bezout(determinant,26);

	inv_determinant = u

	inv_matrix = (inv_determinant * mvint)%26

	return inv_matrix

# mat = [[6,24,1],[13,16,10],[20,17,15]]
# print matrix(mat)
# inv = modular_inverse(mat)
# print matrix(inv)