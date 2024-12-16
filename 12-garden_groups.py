import numpy as np
import sys

def text_to_matrix(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Split each line into characters 
    matrix = [list(line) for line in lines]
    
    return matrix

def dfs(grid, visited, i, j, element, region):
    # Check if the current position is out of bounds or already visited
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] != element:
        return

    # Mark the current position as visited and add it to the region
    visited[i][j] = True
    region.append([i, j])

    # Explore the four possible directions (up, down, left, right)
    dfs(grid, visited, i - 1, j, element, region)
    dfs(grid, visited, i + 1, j, element, region)
    dfs(grid, visited, i, j - 1, element, region)
    dfs(grid, visited, i, j + 1, element, region)

def find_adjacent_regions(grid):
    if not grid:
        return []

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                element = grid[i][j]
                region = []
                dfs(grid, visited, i, j, element, region)
                if region:
                    regions.append(region)

    return regions

# Part one
# def region_price(grid, array):
#     perimeter = 0
#     for point in array:
#         # Up
#         if point[0]-1 >= 0:
#             if grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
#                 print('up')
#                 perimeter += 1
#         if point[0] == 0:
#             perimeter += 1
#         # Right
#         if point[1]+1 <= len(grid[0])-1:
#             if grid[point[0]][point[1]+1] != grid[point[0]][point[1]]:
#                 print('right')
#                 perimeter += 1
#         if point[1] == len(grid[0])-1:
#             perimeter += 1
#         # Down
#         if point[0]+1 <= len(grid)-1:
#             if grid[point[0]+1][point[1]] != grid[point[0]][point[1]]:
#                 perimeter += 1
#         if point[0] == len(grid)-1:
#             print('down')
#             perimeter += 1
#         # Left
#         if point[1]-1 >= 0: 
#             if grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
#                 print('left')
#                 perimeter += 1
#         if point[1] == 0:
#             perimeter += 1
#     print(f"perimeter: {perimeter}")
#     print(array)
#     print(len(array))
#     price = len(array)*perimeter
#     return price

# Part two
def region_price(grid, array):
    perimeter = 0
    for point in array:
        # Up
        if point[0]-1 >= 0 and point[1] >= 0:
            if grid[point[0]-1][point[1]] != grid[point[0]][point[1]] and grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
                print('up')
                perimeter += 1
            if grid[point[0]-1][point[1]-1] == grid[point[0]][point[1]] and grid[point[0]][point[1]-1] == grid[point[0]][point[1]] and grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
                print(point)
                print('up')     
                perimeter += 1
        if point[0] == 0:
            if point == [0, len(grid)-1] and grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
                print(point)
                print('up')     
                perimeter += 1
            if point[1] > 0:
                if grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
                    print(point)
                    print('up')
                    perimeter += 1
            if point[1] == 0:
                print(point)
                print('up')
                perimeter += 1
        # Right
        if point[1]+1 <= len(grid[0])-1 and point[0] >= 0:
            if point == [0,0] and grid[point[0]][point[1]+1] != grid[point[0]][point[1]]:
                print('right')
                perimeter += 1
            if grid[point[0]][point[1]+1] != grid[point[0]][point[1]] and grid[point[0]-1][point[1]] != grid[point[0]][point[1]] :
                print('right')
                perimeter += 1
            if grid[point[0]-1][point[1]+1] == grid[point[0]][point[1]] and grid[point[0]-1][point[1]] == grid[point[0]][point[1]] and grid[point[0]][point[1]+1] != grid[point[0]][point[1]] :
                print('right')
                perimeter += 1
        if point[1] == len(grid[0])-1: 
            if point[0] > 0:
                if grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
                    print('right')
                    perimeter += 1
            if point[0] == 0:
                print('right')
                perimeter += 1
        # Down
        if point[0]+1 <= len(grid)-1 and point[1] >= 0:
            if point[0] == len(grid)-1 and grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
                print('down')
                perimeter += 1
            if grid[point[0]+1][point[1]] != grid[point[0]][point[1]] and grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
                print('down')
                perimeter += 1
            if grid[point[0]+1][point[1]-1] == grid[point[0]][point[1]] and grid[point[0]][point[1]-1] == grid[point[0]][point[1]] and grid[point[0]+1][point[1]] != grid[point[0]][point[1]]:
                print('down')
                perimeter += 1
        if point[0] == len(grid)-1:
            if point[1] > 0:
                if grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
                    print('down')
                    perimeter += 1
            if point[1] == 0:
                print('down')
                perimeter += 1    
        # Left
        if point[1]-1 >= 0 and point[0] >= 0: 
            if point[1] == 0 and grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
                print(point)
                perimeter += 1
            if grid[point[0]][point[1]-1] != grid[point[0]][point[1]] and grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
                print('left')
                print(point)
                perimeter += 1
            if grid[point[0]-1][point[1]-1] == grid[point[0]][point[1]] and grid[point[0]-1][point[1]] == grid[point[0]][point[1]] and grid[point[0]][point[1]-1] != grid[point[0]][point[1]]:
                print('left')
                print(point)
                perimeter += 1
        if point[1] == 0:
            if point[0] > 0:
                if grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
                    print(point)
                    print('left')
                    perimeter += 1
            if point[0] == 0:
                print('left')
                print(point)
                perimeter += 1
                # if grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
                #     print(point)
                #     print('left')
                #     perimeter += 1
            # if point[0] == len(grid) - 1:
            #     if grid[point[0]-1][point[1]] != grid[point[0]][point[1]]:
            #         print('left')
            #         print(point)
            #         perimeter += 1
    
    print(f"perimeter: {perimeter}")
    print(array)
    print(len(array))
    price = len(array)*perimeter
    return price

def price_per_region(grid, matrix):
    regions_total_price = 0
    for row in matrix:
        price = region_price(grid, row)
        regions_total_price += price
    return regions_total_price

def count_elements(matrix): 
    if isinstance(matrix, list):
        return sum(count_elements(sub_matrix) for sub_matrix in matrix) 
    else:
        return 1

# Example grid
grid = [
    [1, 1, 2, 3],
    [1, 2, 2, 3],
    [3, 3, 2, 2],
    [3, 3, 3, 2]
]

# regions = find_adjacent_regions(grid)
# print("Adjacent regions with the same element:")
# for region in regions:
#     print(region)
grid_sample = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'X', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'X', 'O'],
    ['O', 'O', 'O', 'O', 'O']
]

grid_sample1 = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'X', 'X'],
    ['O', 'O', 'O', 'O', 'O']
]

grid_sample2 = [
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'X', 'X', 'O'],
    ['O', 'X', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O']
]

grid_sample4 = [
    ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'F', 'F'],
    ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'C', 'F'],
    ['V', 'V', 'R', 'R', 'R', 'C', 'C', 'F', 'F', 'F'],
    ['V', 'V', 'R', 'C', 'C', 'C', 'J', 'F', 'F', 'F'],
    ['V', 'V', 'V', 'V', 'C', 'J', 'J', 'C', 'F', 'E'],
    ['V', 'V', 'I', 'V', 'C', 'C', 'J', 'J', 'E', 'E'],
    ['V', 'V', 'I', 'I', 'I', 'C', 'J', 'J', 'E', 'E'],
    ['M', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E'],
    ['M', 'I', 'I', 'I', 'S', 'I', 'J', 'E', 'E', 'E'],
    ['M', 'M', 'M', 'I', 'S', 'S', 'J', 'E', 'E', 'E']
]

grid_sample5 = [
    ['A', 'A', 'A', 'A'],
    ['B', 'B', 'C', 'D'],
    ['B', 'B', 'C', 'C'],
    ['E', 'E', 'E', 'C']
]

with open('12-gardengroups.txt', 'r') as file:
    content = file.read()
    grid = text_to_matrix(content)
    adj_reg_unfiltered = find_adjacent_regions(grid)
    adj_reg = []
    # for row in adj_reg_unfiltered:
        # matrix = np.array(row)
        # filtered_matrix = np.array([r for r in matrix if len(r) > 1])
    filtered_matrix = [row for row in adj_reg_unfiltered if len(row) > 1]
    adj_reg = filtered_matrix
    total_regions_price = price_per_region(grid, adj_reg_unfiltered)
    
    # adj_reg = np.array(adj_reg)
    adjacent_regions_size = count_elements(adj_reg)/2
    numpy_grid = np.array(grid)
    grid_size = numpy_grid.size
    print(total_regions_price)
    # print(grid_size)
    # print(adjacent_regions_size)
    # total_single_plants_price = (grid_size - adjacent_regions_size/2) * 4
    # print(total_single_plants_price)
    # total_price = total_regions_price + total_single_plants_price
    # print(total_price)
    # # print(adj_reg)
    # print(grid[127][92])
    # print(grid[128][92])
    # print(grid[129][40])
    # print(grid[127][93])