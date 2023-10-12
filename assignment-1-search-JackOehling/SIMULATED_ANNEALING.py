import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from HILLDESCENT import energyfunction

def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):

	k = maze[0].size
	maze_copy = np.copy(maze)
	best_solution = (maze ,energyfunction(maze, start_cell, goal_state))
	i = 0
	while i < iterations :
		i += 1

		if T == 0 :
			return best_solution
		
		valid = False
		# find a random coordinate that is not the goal state or the start state and check the validity that that maze can be solved
		while not valid :
			random_coord = (np.random.randint(0, k-1), np.random.randint(0, k-1))
			if (not (random_coord == start_cell or random_coord == goal_state)) :
				valid = True
		
		old_value = maze[random_coord]
		maze[random_coord] = np.random.randint(1, k-1)
		# make sure that the maze can be solved if it can't then make it the old value
		if (energyfunction(maze, start_cell, goal_state) == float('inf')) :
			maze[random_coord] = old_value
		
		
		if energyfunction(maze, start_cell, goal_state) > energyfunction(maze_copy, start_cell, goal_state) :
			if np.exp((energyfunction(maze, start_cell, goal_state) + energyfunction(maze_copy, start_cell, goal_state))/ T) < 1:
				maze_copy = np.copy(maze)
				best_solution = (maze, energyfunction(maze, start_cell, goal_state))

		if energyfunction(maze, start_cell, goal_state) < energyfunction(maze_copy, start_cell, goal_state) :
			maze_copy = np.copy(maze)
			best_solution = (maze, energyfunction(maze, start_cell, goal_state))

		
		T = T * decay
		

	'''
	Fill in this function to implement Simulated Annealing.

	The energy function is the same as used for Hill Descent
	and is already imported here for it to be used directly
	(see the energyfunction() function in HILLDESCENT.py).

	With an input temperature 'T' and a decay rate 'decay',
	you should run the algorithm for 'iterations' steps.

	At each step, you should randomly select a valid move,
	and move to that state with probability 1 if the energy
	of the new state is less than the energy of the current state,
	or with probability exp((current_energy - new_energy)/T)
	if the energy of the new state is greater than the current energy.

	After each step, decrease the temperature by 
	multiplying it by the decay rate.

	Your function should return the best solution found,
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	return best_solution
