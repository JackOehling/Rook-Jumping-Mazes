import numpy as np
from VALID_MOVES import valid_moves

def BFS(maze, start):
  '''
  start is talking in terms of position not number

  Fill in this function that uses Breadth First Search to find the shortest path 
  from the start state to the goal state.
    
  Return the matrix (a 2-dimensional numpy array) of shortest path 
  distances from the start cell to each cell. 
    
  If no path exists from the start state to a given cell, that cell should be assigned -1.
    
  The start state should be assigned a path length of 0.
    
  If using print statements to debug, please make sure 
  to remove them before your final submission.
  '''

  size_of_maze = maze.shape[0]

  path_matrix = np.full((size_of_maze, size_of_maze), -1)

  queue = []
  visited = []

  queue.append(start)
  path_matrix[start[0], start[1]] = 0

  while queue:
    node = queue.pop(0)
    visited.append(node)
    neighbors = valid_moves(maze, node)
  
    for neighbor in neighbors:
        if neighbor not in visited and path_matrix[neighbor[0], neighbor[1]] == -1:
            queue.append(neighbor)
            path_matrix[neighbor[0], neighbor[1]] = path_matrix[node[0], node[1]] + 1


  return path_matrix


