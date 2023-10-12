import sys
import numpy as np
from BFS import BFS

def generator(k):
	
	'''
	Fill in this function to generate a k * k maze with random 
	integers between 1 and k-1 (included) in each cell.
	
	Generate a random start state and a random goal state.
	Each of these should be a tuple of integers.
	
	Make sure that the start state and the goal state are not the same.
	
	Set the entry in the maze corresponding to the goal state to 0.
	
	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''

	init_board = np.random.randint(1, k-1, size= (k, k))

	start_cell = ()
	goal_state = ()
	while(start_cell == goal_state) :
		start_cell = (np.random.randint(0, k-1), np.random.randint(0, k-1))
		goal_state = (np.random.randint(0, k-1), np.random.randint(0, k-1))

	init_board[goal_state[1], goal_state[0]] = 0

	return init_board, start_cell, goal_state

def generator_pathcheck(k):
	
	'''
	Copy above function here and modify as follows:
	
	Once a maze is generated, use BFS to check if there is 
	a path from the start state to the goal state.
	
	If there is a valid path, return the maze, the start state, and the goal state.
	
	If not, generate a new maze and repeat.
	'''
	

	bad_board = True

	while bad_board :
		init_board = np.random.randint(1, k-1, size= (k, k))

		start_cell = ()
		goal_state = ()
		while(start_cell == goal_state) :
			start_cell = (np.random.randint(0, k-1), np.random.randint(0, k-1))
			goal_state = (np.random.randint(0, k-1), np.random.randint(0, k-1))

		init_board[goal_state[0], goal_state[1]] = 0

		path_matrix = BFS(init_board, start_cell)

		if path_matrix[goal_state[0], goal_state[1]] != -1:
			bad_board = False

	return init_board, start_cell, goal_state
