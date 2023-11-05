import matplotlib.pyplot as plt
import numpy as np
import random

# Grid size
num_rows = 6
num_cols = 3
num_cells = num_rows * num_cols

# Initialize the grid with all white cells
grid = [['white' for _ in range(num_cols)] for _ in range(num_rows)]

# Set random colors for all cells except row 2, column 2
for i in range(num_rows):
    for j in range(num_cols):
        if i != 1 or j != 1:
            grid[i][j] = random.choice(['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'indigo', 'violet'])

# Generate the random color spectrum
color_spectrum = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'indigo', 'violet']

# Loop through each cell in column 2
for row in range(num_rows):
    col = 1
    # Start at the center cell
    if row == 1:
        chosen_color = grid[row][col]
        
        while chosen_color == 'white':
            # Calculate neighboring cell indices
            neighbor_indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            
            # Choose a random neighboring cell
            neighbor_row, neighbor_col = random.choice(neighbor_indices)
            
            # If the chosen cell is not white, match its color
            if grid[neighbor_row][neighbor_col] != 'white':
                chosen_color = grid[neighbor_row][neighbor_col]
            else:
                # Randomly decide to remain white or choose a color from the spectrum
                chosen_color = random.choice(color_spectrum + ['white'])
        
        grid[row][col] = chosen_color
    else:
        # Update the color of each cell in column 2
        for r in range(1, row+1):
            grid[r][col] = grid[r-1][col]

# Plot the grid
fig, ax = plt.subplots(figsize=(num_cols, num_rows))
for i in range(num_rows):
    for j in range(num_cols):
        color = grid[i][j]
        ax.add_patch(plt.Rectangle((j, num_rows - i - 1), 1, 1, facecolor=color, edgecolor='black'))

plt.axis('equal')
plt.axis('off')
plt.show()
