from __future__ import print_function 
import sys
from matplotlib import pyplot as plt
import numpy as np

def plot(matrix):

	mat = []
	aux = []
	x = []
	y = []
	for i in matrix:
		aux.append(i[1])
		aux.append(i[2])
		mat.append(aux)
		aux = []
	for i in mat:
		x.append(i[0])
		y.append(i[1])
	plt.plot(x, y, 'ro')
	plt.show()



def main():

	#data   Bias   x1     x2   y
	data = [[1.00, 0.08, 0.72, 1.0],
			[1.00, 0.10, 1.00, 0.0],
			[1.00, 0.26, 0.58, 1.0],
			[1.00, 0.35, 0.95, 0.0],
			[1.00, 0.45, 0.15, 1.0],
			[1.00, 0.60, 0.30, 1.0],
			[1.00, 0.70, 0.65, 0.0],
			[1.00, 0.92, 0.45, 0.0],]

	w = [0.2, 1.0, -1.0]

	plot(data)

if __name__ == '__main__':
	main()