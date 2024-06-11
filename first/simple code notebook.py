# Databricks notebook source

import random
## Moving on
def generate_maze(rows, cols):
    # Create a grid with all walls
    maze = [["#" for _ in range(cols)] for _ in range(rows)]

    # Create a stack to keep track of visited cells
    stack = []

    # Choose a random starting cell
    start_row = random.randint(0, rows - 1)
    start_col = random.randint(0, cols - 1)

    # Mark the starting cell as visited
    maze[start_row][start_col] = "S"
    stack.append((start_row, start_col))

    # Depth-first search algorithm
    while stack:
        current_row, current_col = stack[-1]

       # Get the unvisited neighbors of the current cell
        neighbors = []
        if current_row > 1 and maze[current_row - 2][current_col] == "#":
            neighbors.append((current_row - 2, current_col))
        if current_row < rows - 2 and maze[current_row + 2][current_col] == "#":
            neighbors.append((current_row + 2, current_col))
        if current_col > 1 and maze[current_row][current_col - 2] == "#":
            neighbors.append((current_row, current_col - 2))
        if current_col < cols - 2 and maze[current_row][current_col + 2] == "#":
            neighbors.append((current_row, current_col + 2))

        if neighbors:
            # Choose a random neighbor
            next_row, next_col = random.choice(neighbors)

            # Remove the wall between the current cell and the chosen neighbor
            maze[(current_row + next_row) // 2][(current_col + next_col) // 2] = " "

            # Mark the chosen neighbor as visited
            maze[next_row][next_col] = " "
            stack.append((next_row, next_col))
        else:
            # Backtrack if there are no unvisited neighbors
            stack.pop()

    # Mark the last cell as the exit
    maze[rows - 1][cols - 1] = "E"

    return maze

# Generate a 10x10 maze
maze = generate_maze(10, 10)
print(maze)

