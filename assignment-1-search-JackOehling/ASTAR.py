import heapq
import numpy as np
from VALID_MOVES import valid_moves

def H_score(node, goal, n):
	'''
	Fill in this function to return the heuristic value of the current node.

	Compute heuristic as the Manhattan distance between the 
	current node and the goal state, divided by 
	the largest possible jump value.

	n is the dimensionality of the maze (n x n).

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''

	#changed the heuristic
	heuristic = (abs(node[0] - goal[0]) + abs(node[1] - goal[1])) / (n - 1)



	return heuristic


def ASTAR(maze, start, goal) :
	pqueue = []
	visited = set()
	heapq.heappush(pqueue, (H_score(start, goal, maze[0].size), 0, (start, ())))

	while pqueue:
		heuristic, cost, (node, path) = heapq.heappop(pqueue)
		path = path + (node,)
		visited.add(node)
		if node == goal:
			return len(path)-1, path
		for neighbor in valid_moves(maze, node):
			if neighbor not in visited:
				visited.add(neighbor)
				G_score = cost + 1
				heapq.heappush(pqueue, (G_score + H_score(neighbor, goal, maze[0].size), G_score, (neighbor, path)))	

	'''
	Fill in this function that uses A* search to find the shortest 
	path using the heuristic function H_score defined above.

	Return the length of the shortest path from the start state 
	to the goal state, and the path itself.

	Your return statement should be of the form:
	return len(path)-1, path

	where path is a list of tuples, corresponding to the 
	path and includes the start state.

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	










