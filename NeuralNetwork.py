#!/usr/bin/python3
#	____ _    _ ____ ____ 
#	|__| |    | |    |___ 
#	|  | |___ | |___ |___ 
#
#NEURALNETWORK CORE
import numpy as np 
import random 
import os

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x)
	
def tanh_prime(x):
    return 1.0 - x**2

class nn(): 
	def __init__(self, layers, activation='tanh'):
		if activation == 'sigmoid':
			self.activation = sigmoid
			self.activation_prime = sigmoid_prime
		elif activation == 'tanh':
			self.activation = tanh
			self.activation_prime = tanh_prime
		# Set weights
		self.weights = []
		# layers = [2,2,1]
		# range of weight values (-1,1)
		# input and hidden layers - random((2+1, 2+1)) : 3 x 3  
		for i in range(1, len(layers) - 1):
			r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
			self.weights.append(r)
		# output layer - random((2+1, 1)) : 3 x 1
		r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
		self.weights.append(r)

	def ajust(self, X, y, learning_rate=0.0001, epochs=100000000):
		print('X = ', str(X)[1:-1])
		print('Y = ', str(y)[1:-1])			
		# Add column of ones to X
		# This is to add the bias unit to the input layer
		ones = np.atleast_2d(np.ones(X.shape[0]))
		X = np.concatenate((ones.T, X), axis=1)
		for k in range(epochs):
			i = np.random.randint(X.shape[0])
			a = [X[i]]	
			for l in range(len(self.weights)):
				dot_value = np.dot(a[l], self.weights[l])
				activation = self.activation(dot_value)
				a.append(activation)
		   	# output layer
			error = y[i] - a[-1]
			#print(error,end='\r')
			nablas = [error * self.activation_prime(a[-1])]
			# we need to begin at the second to last layer 
			# (a layer before the output layer)
			for l in range(len(a) - 2, 0, -1): 
				nablas.append(nablas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))
			# reverse
			# [level3(output)->level2(hidden)]  => [level2(hidden)-level3(output)]
			nablas.reverse()
				# backpropagation
				# 1. Multiply its output delta and input activation 
				#   to get the gradient of the weight.
				# 2. Subtract a ratio (percentage) of the gradient from the eight.
			for i in range(len(self.weights)):
				layer = np.atleast_2d(a[i])
				delta = np.atleast_2d(nablas[i])
				self.weights[i] += learning_rate * layer.T.dot(delta)
		#if k % 1 == 0: print('epochs: ', k, end='/r')
			#if 1: print(self.weights,end ='\n')
			if k % 1000 == 0: print('e',': %0.3E' % k, '%0.3E' % epochs, ', at %0.2E' % learning_rate, 'h', 'units, MATRIX:', end='\r')

	def predict(self, x):
		a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)      
		for l in range(0, len(self.weights)):
			a = self.activation(np.dot(a, self.weights[l]))
		return a




