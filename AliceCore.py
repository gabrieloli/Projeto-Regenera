#!/usr/bin/python3
try:
	import numpy as np 
except:
	pass
try:
	import time
except:
	pass
try:
	import random 
except:
	pass
try:
	import sys 
except:
	pass
try:
	import os 
except:
	pass

try:
	from NeuralNetwork import *
except:
	pass

try:
	from KnowledgeCore import *
except:
	pass

try:
	from EmotionalCore import *
except:
	pass

class AliceCore():

	def begin(learning_rate,epochs):
		os.system('clear')

		print('#	____ _    _ ____ ____        #')
		print('#	|__| |    | |    |___	     #')
		print('#	|  | |___ | |___ |___	     #')
		print('#				     #')
		time.sleep(0.25)
		print("""Welcome to the
		 Auto
		 | Learning
		 | | Intelligent
		 | | | Convolutional
		 | | | | Ecosystem
		 | | | | |  Project
		 A L I C E
			""")
		time.sleep(0.35)
		print("Verifying matrix integrity now:")
		time.sleep(0.5)
		CORES = ['NeuralNetwork','KnowledgeCore','EmotionalCore']
		AliceCore.check_matrix_integrity(CORES)
		time.sleep(0.25)
		print('\nVAR: ', 'h', 'Hammad -> %0.2E' % learning_rate)
		time.sleep(0.25)
		print('VAR: ', 'e', 'Epochs -> %0.2E' % epochs)
		time.sleep(0.05)
		AliceCore.evaluate_chaos(learning_rate,epochs)

	def check_loaded(module_name):	
		ok = 0
		problematic = 0
		for i in module_name:
			time.sleep(random.uniform(0.15, 0.75))
			print('LOADED: ',i,' Core ->', (i in sys.modules))
			if (i in sys.modules): ok += 1
			if not(i in sys.modules): problematic += 1
		return (ok,problematic)
	def check_matrix_integrity(cores):
		ok, problematic = AliceCore.check_loaded(cores)
		total = ok + problematic
		percentage = 100/total
		integrity = 100-problematic*percentage
		print("Matrix integrity: ", "{0:.2f}".format(round(integrity,3)), "%")
	def evaluate_chaos(learning_rate,epochs):
		print("\nBooting Up Convolutional Core")
		kc.assimilate(learning_rate,epochs)
	def evaluate_data(name, input_data):
		print(kc.acquire(name, input_data))
		return kc.acquire(name, input_data)

