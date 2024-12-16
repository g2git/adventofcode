loopcount = 0

def text_to_matrix(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Split each line into characters 
    matrix = [list(line) for line in lines]
    
    return matrix

def move_up(position, matrix):
    pos = position
    mat = matrix
    # position[row, colomn]
    while (pos[0] != 0) and (mat[pos[0]-1][pos[1]] != "#") and (mat[pos[0]-1][pos[1]] != "^") and (mat[pos[0]-1][pos[1]] != "O"):
         mat[pos[0]-1][pos[1]] = "^"
         pos = [pos[0]-1, pos[1]]
    if pos[0] == 0:
        return pos, mat
    elif mat[pos[0]-1][pos[1]] == "^":
        global loopcount 
        loopcount += 1
        for k in mat:
            print(k)
        return pos, mat       
    else:
        return move_right(pos, mat)
        
def move_right(position, matrix):
    pos = position
    mat = matrix
    # position[row, colomn]
    while (pos[1] != len(mat[pos[0]])-1) and (mat[pos[0]][pos[1]+1] != "#") and (mat[pos[0]][pos[1]+1] != ">") and (mat[pos[0]][pos[1]+1] != "O"):
         mat[pos[0]][pos[1]+1] = ">"
         pos = [pos[0], pos[1]+1]
    if pos[1] == len(mat[pos[0]])-1:
        return pos, mat
    elif mat[pos[0]][pos[1]+1] == ">":
        global loopcount 
        loopcount += 1
        for k in mat:
            print(k)
        return pos, mat
    else:
        return move_down(pos, mat)
    
def move_down(position, matrix):
    pos = position
    mat = matrix
    # position[row, colomn]
    while (pos[0] != len(matrix)-1) and (mat[pos[0]+1][pos[1]] != "#") and (mat[pos[0]+1][pos[1]] != "v") and (mat[pos[0]+1][pos[1]] != "O"):
         mat[pos[0]+1][pos[1]] = "v"
         pos = [pos[0]+1, pos[1]]
    if pos[0] == len(matrix)-1:
        return pos, mat
    elif mat[pos[0]+1][pos[1]] == "v":
        global loopcount 
        loopcount += 1
        for k in mat:
            print(k)
        return pos, mat
        
    else:
        return move_left(pos, mat)

def move_left(position, matrix):
    pos = position
    mat = matrix
    # position[row, colomn]
    while (pos[1] != 0) and (mat[pos[0]][pos[1]-1] != "#") and (mat[pos[0]][pos[1]-1] != "<") and (mat[pos[0]][pos[1]-1] != "O"):
         mat[pos[0]][pos[1]-1] = "<"
         pos = [pos[0], pos[1]-1]
    if pos[1] == 0:
        return pos, mat
    elif mat[pos[0]][pos[1]-1] == "<":
        global loopcount 
        loopcount += 1
        for k in mat:
            print(k)
        return pos, mat
    else:
        return move_up(pos, mat)
    
# Function to find the position of an element 
def find_position(matrix, element):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): 
            if matrix[i][j] == element:
                return [i, j]
    return None

with open('6-guardgallivant.txt', 'r') as file:
    content = file.read()
    mapmatrix = text_to_matrix(content)
    # print(len(mapmatrix))
    
    # Sample 2D matrix
    sample_matrix = [
        ['-', '#', '#', '-', '-'],
        ['-', '-', '-', '-', '#'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '^', '-', '-'],
        ['-', '-', '-', '#', '-']
    ] 


    position = find_position(mapmatrix, "^")
    # posi, matr = move_up(position, sample_matrix)
    # for r in matr:
    #     print(r)
        
    
    # Iterate through the matrix with indices
    rows = len(mapmatrix)
    cols = len(mapmatrix[0])
    for row in range(0, rows):
        for col in range(0, cols):
            if mapmatrix[row][col] != "#" and mapmatrix[row][col] != "^":
                _matr = [row[:] for row in mapmatrix]
                _matr[row][col] = "O"
                move_up(position, _matr)
    
    print(loopcount)
    
    # Element to count
    element = '^'
    # Initialize count
    count = 0
    # Count occurrences using nested loops 
    for row in sample_matrix:
        for item in row:
            if item == element:
                count += 1
                
    # print(f"Number of occurrences of '{element}': {count}")
    # print(posi)
    
