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


def predict(inputs, weights):
	threshold = 0.0
	total_activation = 0.0
	for input, weight in zip(inputs,weights):
		total_activation += input*weight
	return 1.0 if total_activation >= threshold else 0.0

#Calculate predict accuracy, provided inputs and assoc weight
def accuracy(matrix, weights):
	num_correct = 0.0
	preds = []
	for i in range(len(matrix)):
		#get predicted classification
		pred = predict(matrix[i][:-1], weights)
		#check if prediction is accurate
		if pred == matrix[i][-1] : num_correct += 1.0
	print("Predictions: ", preds)
	#return overall prediction accuracy
	return num_correct/float(len(matrix))

#train the perceptron on the data found in the matrix
#trained weights are returned at the end of the func
def train_weights(matrix, weights, nb_epoch=10, l_rate=1.0, do_plot=False, stop_early=True, verbose=True):
	#Iterate for the number of epochs requested
	for epoch in range(nb_epoch):
		#calculate the current accuracy
		cur_acc = accuracy(matrix, weights)
		#Print out information
		print("\nEpoch %d \nWeights: "%epoch,weights)
		print("Accuracy: ", cur_acc)

		#check if finished the training
		if curr_acc == 1.0 and stop_early: break

		#check if should plot the current results
		if do_plot: plot(matrix, weights)

		#iterate over each training input
		for i in range(len(matrix)):
			#calculate predict
			prediction = predict(matrix[i][:-1],weights)
			# calculate error
			error = matrix[i][-1]-prediction

			if verbose:
				print("Training on data at index %d.."%i)

			#iterate over each weight and update it
			for j in range(len(weights)):
				if verbose:
					sys.stdout.write("\tWeight[%d]: %0.5f --> " % (j, weights[j]) )
				weights[j] = weights[j]+(l_rate*error*matrix[i][j])

				if verbose:
					sys;stdout.write("%0.5f\n"%weights[j])
	#plots the final result
	plot(matrix, weights)
	return weights

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

	train_weights(data, weights = w, nb_epoch = 10, l_rate = 1.0, do_plot = True, stop_early = True)

if __name__ == '__main__':
	main()