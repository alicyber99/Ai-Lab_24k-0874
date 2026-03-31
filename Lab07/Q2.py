#1. Constraint Model:
#Each cell is a variable 0 or 1 (0 = water, 1 = land).
#Grid values are already given, so we fix the variables.
#2. Finding Boundary Edges:
#For each land cell, check 4 neighbors (up, down, left, right).
#If neighbor is water or outside the grid → add 1 to perimeter.
#3. OR-Tools and Perimeter Calculation:
#We create binary variables for cells (land/water)
#Then we check neighbors and sum perimeter.

from ortools.sat.python import cp_model

def largest_island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    model = cp_model.CpModel()
    
    x = {}
    for i in range(rows):
        for j in range(cols):
            x[(i,j)] = model.NewBoolVar(f'x_{i}_{j}')
            model.Add(x[(i,j)] == grid[i][j])  
    
    perimeter = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if ni < 0 or nj < 0 or ni >= rows or nj >= cols or grid[ni][nj] == 0:
                        perimeter += 1
                        
    return perimeter

grid = [
    [1,1,0,0],
    [1,1,0,1],
    [0,0,1,1],
    [0,0,1,0]
]

print("Perimeter:", largest_island_perimeter(grid))

#Output: Perimeter: 14
