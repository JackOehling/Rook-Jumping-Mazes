import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR


def energyfunction(maze, start, goal):
	'''
	Compute the energy as the sum of the shortest path length 
	from the start state to the goal state (computed using A*)
	and the number of cells that are not reachable from the 
	start state (computed using BFS).

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	energy = -1

	if (ASTAR(maze, start, goal) == None) :
		length_of_shortest_path = float('inf')
	else : 
		length_of_shortest_path, path = ASTAR(maze, start, goal)

	path_matrix = BFS(maze, start)
	nodes_missed = np.where(path_matrix == -1)

	energy = length_of_shortest_path + len(nodes_missed[0])
	return energy



def HILLDESCENT(maze, start_cell, goal_state, iterations):
	'''
	Fill in this function to implement Hill Descent local search.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	k = maze[0].size
	i = 0

	changed_maze = np.copy(maze)
	maze_copy = np.copy(maze)

	# for the number iterations
	while i < iterations :
		i += 1
		
		valid = False
		# find a random coordinate that is not the goal state or the start state and check the validity that the maze can be solved
		while not valid :
			random_coord = (np.random.randint(0, k-1), np.random.randint(0, k-1))
			if (not (random_coord == start_cell or random_coord == goal_state)) :
				valid = True
		
		old_value = changed_maze[random_coord]
		changed_maze[random_coord] = np.random.randint(1, k-1)
		# make sure that the maze can be solved if it can't then make it the old value
		if (energyfunction(changed_maze, start_cell, goal_state) == float('inf')) :
			changed_maze[random_coord] = old_value
		
		# if that random point did not decrease the energy in the original maze to a value less than the last iterations
		if energyfunction(changed_maze, start_cell, goal_state) >= energyfunction(maze_copy, start_cell, goal_state) :
			# then keep the old maze
			changed_maze = np.copy(maze_copy)

		if energyfunction(changed_maze, start_cell, goal_state) <= energyfunction(maze_copy, start_cell, goal_state) :
			# update the new maze
			maze_copy = np.copy(changed_maze)

	# return the optimal maze that was updated and the energy of the maze
	return (changed_maze, energyfunction(changed_maze, start_cell, goal_state))



def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
	'''
	Fill in this function to implement Hill Descent local search with Random Restarts.

	For a given number of searches (num_searches), run hill descent search.

	Keep track of the best solution through all restarts, and return that.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	You will also need to keep a separate copy of the original maze
	to use when restarting the algorithm each time.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	i = 0

	changed_maze = np.copy(maze)
	maze_copy = np.copy(maze)
	original_maze = np.copy(maze)

	best_solution = (changed_maze, energyfunction(changed_maze, start_cell, goal_state))

	while i < num_searches :
		i += 1
		
		# the mazes must be the original every time the while loop runs
		changed_maze = np.copy(original_maze)
		maze_copy = np.copy(original_maze)

		# find the best mazes from each of the two hill descents that were run
		best_maze_1, best_energy_1 = HILLDESCENT(changed_maze, start_cell, goal_state, iterations)
		best_maze_2, best_energy_2 = HILLDESCENT(maze_copy, start_cell, goal_state, iterations)

		# check to see if the the first hill descent is less that the current best and also less than the second run of hill descent
		if best_solution[1] >= best_energy_1 and best_energy_1 <= best_energy_2 :
			best_solution = (best_maze_1, best_energy_1)

		# check to see if the the second hill descent is less that the current best and also less than the first run of hill descent
		if best_solution[1] >= best_energy_2 and best_energy_2 <= best_energy_1:
			best_solution = (best_maze_2, best_energy_2)

		# check to see if the the current hill descent is less that the first run of hill descent
		# and also less than the second run of hill descent then it just stays the same
		# I understand that this isn't needed but I decided to add it because it helps the reader see what happens when the first ifs aren't true
		if best_solution[1] <= best_energy_2 and best_solution[1] <= best_energy_1:
			best_solution = best_solution

		
	# check the energy of the original maze that was passed in
	original_energy = energyfunction(original_maze, start_cell, goal_state)
	# if the new best solution energy is less than the original energy return the best solution
	# if it isn't thene just keep the original maze and energy
	if best_solution[1] < original_energy :
		return best_solution
	else :
		return (original_maze, original_energy)



def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
	'''
	Fill in this function to implement Hill Descent local search with Random uphill steps.

	At each iteration, with probability specified by the probability
	argument, allow the algorithm to move to a worse state.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	k = maze[0].size
	i = 0
	maze_copy = np.copy(maze)
	original_maze = np.copy(maze)

	best_solution = (maze, energyfunction(maze, start_cell, goal_state))

	# for the number iterations
	while i < iterations :
		i += 1
		valid = False
		# find a random coordinate that is not the goal state or the start state and check the validity that the maze can be solved
		while not valid :
			random_coord = (np.random.randint(0, k-1), np.random.randint(0, k-1))
			if (not (random_coord == start_cell or random_coord == goal_state)) :
				valid = True
		
		old_value = maze[random_coord]
		maze[random_coord] = np.random.randint(1, k-1)
		# make sure that the maze can be solved if it can't then make it the old value
		if (energyfunction(maze, start_cell, goal_state) == float('inf')) :
			maze[random_coord] = old_value
		
		# see if the new value added deacreased the energy of the maze 
		if energyfunction(maze, start_cell, goal_state) < energyfunction(maze_copy, start_cell, goal_state) :
			# if it is update the copied maze for the next iteration and also update the best current solution
			maze_copy = np.copy(maze)
			best_solution = (maze, energyfunction(maze, start_cell, goal_state))
		else :
			maze = np.copy(maze_copy)
			
		# This is the uphill step part
		# if the energy is increased by the new random change and with a small probability we can keep this change even though it hurts
		# the best energy
		if energyfunction(maze, start_cell, goal_state) > energyfunction(maze_copy, start_cell, goal_state) and np.random.rand(0, 1) <= probability:
			maze_copy = np.copy(maze)
			best_solution = (maze, energyfunction(maze, start_cell, goal_state))
		else :
			maze = np.copy(maze_copy)

	# check the energy of the original maze that was passed in
	original_energy = energyfunction(original_maze, start_cell, goal_state)
	# if the new best solution energy is less than the original energy return the best solution
	# if it isn't thene just keep the original maze and energy
	if best_solution[1] < original_energy :
		return best_solution
	else :
		return (original_maze, original_energy)