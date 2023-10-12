import numpy as np

def valid_moves(maze, node):
	neighbors=[]
	
	rows = node[0]
	columns = node[1]
	
	amount_of_jumps = maze[rows][columns]
	
	if rows + amount_of_jumps < maze[0].size :
		neighbors.append(((rows + amount_of_jumps), columns))

	if rows - amount_of_jumps >= 0 :
		neighbors.append(((rows - amount_of_jumps), columns))

	if columns - amount_of_jumps >= 0 :
		neighbors.append((rows, (columns - amount_of_jumps)))

	if columns + amount_of_jumps < maze[0].size :
		neighbors.append((rows, (columns + amount_of_jumps)))

		
	'''
	Fill in this function to return a list of "valid" neighbors 
	for the current node in the rook-jumping-maze.
	
	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''

	return neighbors
