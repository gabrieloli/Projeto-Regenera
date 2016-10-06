#!/usr/bin/python3
#	____ _    _ ____ ____ 
#	|__| |    | |    |___ 
#	|  | |___ | |___ |___ 
#

import numpy as np 
import time
import random 
import sys 
import os 
try:
	from AliceCore import *
except:
	pass

learning_rate=0.001
epochs=int(10E5)

if __name__ == '__main__':
	AliceCore.begin(learning_rate,epochs)
	
	print('')
	while True:
		name = input('DATA ID: ')
		input_data = input('INPUT: ')
		input_data = list(map(float, input_data.split(',')))
		print(AliceCore.evaluate_data(name, input_data))
