#!/usr/bin/env python

import numpy as np

#establish a variable for initial population size.

#currentPop = input("Type the starting population of indiviuduals: ")
currentPopulation = int(input("Initial population size: "))

#establish variable for carrying capacity
#maxPop = input("Type the carrying capacity of the enviroment: ")
carryingCapacity = int(input("Population carrying capacity: "))

#establish a variable for number of generation for growth
#genCount = input("Type the number of generations to be Simulated: ")
generationCount = int(input("Number of generations: "))

#est. variable for  mean/average offspring per individuals per generation
meanOffspring = 1

# loop generation count times
for i in range(0, generationCount):
# {
	#show currentPopulation
	print (currentPopulation)

	#oldPopOff <- poisson (mean: meanOffspring, size : currentPop)
	oldPopulationOffspring = np.random.poisson(meanOffspring,currentPopulation)

	# currentPop <- sum of all currentPopOffspring
	currentPopulation = 0
	for j in oldPopulationOffspring:
	#for each item in oldPopulationOffspring, set j to the item
		currentPopulation = currentPopulation + j
	
	# if currentPopulation > carryingCapacity
	if currentPopulation > carryingCapacity:

	# currentPop <- carryingCapacity
		currentPopulation = carryingCapacity
	#}
	
#}


#pop = np.ones(p) + np.random.uniform(-0.5,0.5,p)

#establish a system for population to predict offspring per individual at random.

#establish the number of generations in the experiment.

#Define the carrying capacity.
