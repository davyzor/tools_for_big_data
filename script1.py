"""Write a script which reads a matrix from a file like this one and solves the linear matrix equation Ax=b where b is the last column of the input-matrix and A is the other columns.

"""
import numpy as np 

def from_file_to_matrix(filename):

	matrix = []
	array = []
	with open(filename) as f:
		for line in f:
			data = line.split(',')
			for element in data:
				array.append(int(element))
			matrix.append(array)
			array = []
	m = np.matrix(matrix)

	return m

A = from_file_to_matrix('matrix.txt')
print A

#indexing the number of columns, since shape returns you (#rows, #columns)
last_column_index = A.shape[1] - 1
b = A[:, last_column_index]

A = np.delete(A,-1,1)

x = np.linalg.solve(A, b)

#check that the result is true
print np.allclose(np.dot(A, x), b)


