# Function to generate all possible paths of length 10
def generate_paths(matrix, x, y, path, paths, length):
    rows, cols = len(matrix), len(matrix[0])
    
    # Check if the current position is out of bounds
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return
    
    # Add the current position to the path
    # path.append([x, y])
    path.append(matrix[x][y])
    
    # If the path length is 10, add the path to the list of paths
    if len(path) == length:
        paths.append(list(path))
    else:
        # Move down
        generate_paths(matrix, x + 1, y, path, paths, length)
        # Move right
        generate_paths(matrix, x, y + 1, path, paths, length)
        # Move up
        generate_paths(matrix, x - 1, y, path, paths, length)
        # Move left
        generate_paths(matrix, x, y - 1, path, paths, length)
    
    # Remove the current position from the path (backtracking)
    path.pop()
    
def text_to_matrix(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Split each line into characters 
    matrix = [list(line) for line in lines]
    
    return matrix

# Function to find positions of all elements that equal '0'
def find_zero_positions(matrix):
    positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                positions.append([i, j])
    return positions

# Function to convert all elements to integers 
def convert_matrix_to_integers(matrix):
    return [[int(element) for element in row] for row in matrix]

def count_zero_to_nine_paths(matrix):
    path = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = matrix.count(path)
    return count

def is_path_good(matrix, array):
    path = []
    for ar in array:
        path.append(matrix[ar[0]][ar[1]])
    if path == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    else: 
        return False


# Sample grid matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# # List to store all possible paths
# paths = []

# # Generate all possible paths of length 10 starting from the top-left corner (0, 0)
# generate_paths(matrix, 0, 0, [], paths, 10)


# # Print all possible paths
# for path in paths:
#     print(path)



with open('10-hoofit.txt', 'r') as file:
    content = file.read()
    textmatrix = text_to_matrix(content)
    gridmatrix = convert_matrix_to_integers(textmatrix)
    zero_positions = find_zero_positions(gridmatrix)

    # height_counter = []
    # for pos in zero_positions:
    #     paths = []
    #     nines = []
    #     generate_paths(gridmatrix, pos[0], pos[1], [], paths, 10)
    #     for p in paths:
    #         if is_path_good(gridmatrix, p):
    #             nines.append(p[9])
    #     # Convert each list to a tuple and add to a set 
    #     unique_rows = set(tuple(row) for row in nines) 
    #     # Get the number of distinct rows 
    #     distinct_count = len(unique_rows)
    #     height_counter.append(distinct_count)
                
    
    # print(height_counter)
    # print(sum(height_counter))
    
    #Part two
    counter = []
    for pos in zero_positions:
        paths = []
        generate_paths(gridmatrix, pos[0], pos[1], [], paths, 10)
        count = count_zero_to_nine_paths(paths)
        counter.append(count)
    print(sum(counter))
        
