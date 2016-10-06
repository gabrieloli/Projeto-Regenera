#!/usr/bin/python3
#	____ _    _ ____ ____ 
#	|__| |    | |    |___ 
#	|  | |___ | |___ |___ 
#
#Knowledge Core

from NeuralNetwork import *
#from knn_algo import *

class kc():
	def assimilate(learning_rate,epochs):
		
		names = ['not','rain','sprinkler','grass_wet']
		for l in names:
			print('')
			print(l)
			multiplier = eval('len(x_'+l+'.T)')
			print('Constant of complexity at:', multiplier)			
			epochs = epochs+multiplier
			print('Therefore: %0.2E' % epochs)
			eval('nn_'+l+'.ajust(x_'+l+',y_'+l+','+str(learning_rate)+','+str(epochs)+')')
			
	def assimilate_singular(data):
		print(data)
		eval('nn_'+data+'.ajust(x_'+data+',y_'+data+', epochs=10000)')

	def acquire(name, input_data):
		print(input_data) 
		return eval(("nn_"+name+".predict(" + str(input_data) + ")"))




"""
NOT
"""

nn_not = nn([1,10,1])
x_not = np.array([[1],
		  [0]])
y_not = np.array([[0],
		  [1]])


"""
AND
"""

nn_and = nn([2,10,1])
x_and = np.array([[0,0],
		  [0,1],
		  [1,0],
		  [1,1]])
y_and = np.array([[0],
		  [0],
		  [0],
		  [1]])

"""
Rain:

____|_____|_T_|_F_
Sun | Wet |
_1__|_0___|_0_|_1_
_0__|_0___|_.5_|_0.5_
_0__|_1___|_1_|_0_

"""

nn_rain = nn([2,100,2])
x_rain = np.array([[1,0],
		   [0,0],
		   [0,1]])
y_rain = np.array([[0,1],
		   [0.5,0.5],
		   [1,0]])

"""

Sprinkler:

Rain|--|_T_|_F_ 
_1__|--|_0_|_1_
_0__|--|_1_|_0_

"""

nn_sprinkler = nn([1,100,2])
x_sprinkler = np.array([[1],
			[0]])
y_sprinkler = np.array([[0,1],
			[1,0]])

"""

Grass Wet:

Sprinkler | Rain |--| True | False|
___0______|__0___|--|__0___|__1___|
___0______|__1___|--|__1___|__0___|
___1______|__0___|--|__1___|__0___|
___1______|__1___|--|__1___|__0___|

"""

nn_grass_wet = nn([2,100,2])
x_grass_wet = np.array([[0,0],
			[0,1],
			[1,0],
			[1,1]])
y_grass_wet = np.array([[0,1],
			[1,0],
			[1,0],
			[1,0]])

"""
Check if grass is wet:
"""
def grass_is_wet(sun, wet, rain, sprinkler):

	input_rain = str(sun)+','+str(wet)
	input_rain = list(map(float, input_rain.split(',')))
	rain = kc.acquire('rain', input_rain)
	rain = list(map(float, rain))
	rain = rain[0]

	input_sprinkler = str(sprinkler)
	input_sprinkler = list(map(float, input_sprinkler))
	sprinkler = kc.acquire('sprinkler', input_sprinkler)
	sprinkler = list(map(float, sprinkler))
	sprinkler = sprinkler[0]

	input_grass_wet = str(sprinkler) + ',' + str(rain)
	input_grass_wet = list(map(float, input_grass_wet.split(',')))
	grass_wet = kc.acquire('grass_wet', input_grass_wet) 
	return(grass_wet)

