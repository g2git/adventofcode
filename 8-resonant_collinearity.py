from collections import Counter

def count_occurrences(matrix, element): 
    count = 0 
    for row in matrix: 
        for item in row: 
            if item == element:
                count += 1 
    return count

# Function to get all distinct elements in a 2D matrix
def get_distinct_elements(matrix):
    unique_elements = set()
    for row in matrix:
        for element in row:
            if element != ".":
                unique_elements.add(element)
    return list(unique_elements)

def get_all_elements_count(matrix):
    # Element must occur more than 1 time
    all_elements = []
    for row in matrix:
        for element in row:
            if element != ".":
                all_elements.append(element)
    # Count the occurrences of each element
    element_counts = Counter(all_elements)
    # Filter out elements that occur only once
    filtered_array = [element for element in all_elements if element_counts[element] > 1]
    return len(filtered_array)

def text_to_matrix(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Split each line into characters 
    matrix = [list(line) for line in lines]
    
    return matrix

# Function to find the indexes of all occurrences of an element
def find_indexes(matrix, element):
    indexes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                indexes.append([i, j])
    return indexes

# Function to return the indexes of an antinode
def find_antinode(cor1, cor2):
    distance = [cor1[0]-cor2[0], cor1[1]-cor2[1]]
    coordinates  = [a + b for a, b in zip(cor1, distance)]
    return coordinates

# Function to return the indexes of all T-antinodes
def find_T_antinodes(cor1, cor2, matrix):
    coords = []
    coordinates = cor1
    distance = [cor1[0]-cor2[0], cor1[1]-cor2[1]]
    while (0 <= coordinates[0] < len(matrix)) and (0 <= coordinates[1] < len(matrix[0])):
        coordinates  = [a + b for a, b in zip(coordinates, distance)]
        if (0 <= coordinates[0] < len(matrix)) and (0 <= coordinates[1] < len(matrix[0]) and matrix[coordinates[0]][coordinates[1]] == "."):
            coords.append(coordinates)
        
    return coords

def return_antinode_array(array):
    result = []

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:  # Avoiding adding the element to itself
                result.append(find_antinode(array[i], array[j]))

    return result

def get_all_T_antinodes(array, matrix):
    result = []

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:  # Avoiding adding the element to itself
                for t in find_T_antinodes(array[i], array[j], matrix):
                    result.append(t)

    return result

def count_nodes_in_map(matrix, antinodes_array):
    matr = []
    for ar in antinodes_array:
        if (0 <= ar[0] < len(matrix)) and (0 <= ar[1] < len(matrix[0])):
            matr.append(ar)
    return matr, len(matr)

def rewrite_map(matrix, array):
    matr = matrix
    for ar in array:
        if (0 <= ar[0] < len(matrix)) and (0 <= ar[1] < len(matrix[0])) and matrix[ar[0]][ar[1]] == ".":
            matr[ar[0]][ar[1]] = "#"
    return matr

def remove_duplicates(matrix):
    # Remove duplicate rows
    unique_matrix = []
    for row in matrix:
        if row not in unique_matrix:
            unique_matrix.append(row)

    return unique_matrix



with open('8-resonantcollinearity.txt', 'r') as file:
    content = file.read()
    gridmatrix = text_to_matrix(content)
    
    # Get the distinct elements
    distinct_elements = get_distinct_elements(gridmatrix)
    print(distinct_elements)
    
    # Find the indexes of the element
    indexes = find_indexes(gridmatrix, "X")

    print(f"Indexes of X: {indexes}")
    
    # print(return_antinode_array(indexes))
    # ix =return_antinode_array(indexes)
    # num = count_nodes_in_map(gridmatrix, ix)
    # print(f"number of X antinodes: {num}")
    
    
    copied_gridmatrix = [row[:] for row in gridmatrix]
    count = 0
    cleaned_list = []
    
    for d in distinct_elements:
        ind = find_indexes(gridmatrix, d)
        antinodes = return_antinode_array(ind)
        mat, co= count_nodes_in_map(gridmatrix, antinodes)
        for x in mat:
            cleaned_list.append(x)
        count += co

        
    unique_list = remove_duplicates(cleaned_list)
    ul = len(unique_list)
    print(f"Unique_list size: {ul}")
    print(f"Node count: {count}")
    
    # Part two
    t_antinodes_list = []
    for di in distinct_elements:
        inds = find_indexes(gridmatrix, di)
        t_antinodes = get_all_T_antinodes(inds, gridmatrix)
        for x in t_antinodes:
            t_antinodes_list.append(x)
 
    t_antinodes_list = remove_duplicates(t_antinodes_list)
    print(len(t_antinodes_list))
    ln = rewrite_map(copied_gridmatrix, t_antinodes_list)
    print(count_occurrences(ln, "#"))
    print(get_all_elements_count(gridmatrix))
    print(get_all_elements_count(gridmatrix) + len(t_antinodes_list))
