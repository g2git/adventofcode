import re

def text_to_matrix(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Split each line into characters 
    matrix = [list(line) for line in lines]
    
    return matrix


def get_verticals(matrix):
    verticals = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for col in range(cols):
        vertical = []
        for row in range(rows):
            vertical.append(matrix[row][col])
        verticals.append(''.join(vertical))
    
    return verticals


def get_diagonals(matrix):
    diagonals = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Get diagonals from top-left to bottom-right
    for col in range(cols):
        diagonal = []
        x, y = 0, col
        while x < rows and y < cols:
            diagonal.append(matrix[x][y])
            x += 1
            y += 1
        diagonals.append(''.join(diagonal))
    
    for row in range(1, rows):
        diagonal = []
        x, y = row, 0
        while x < rows and y < cols:
            diagonal.append(matrix[x][y])
            x += 1
            y += 1
        diagonals.append(''.join(diagonal))
    
    return diagonals


def reverse_matrix(matrix):
    # Reverse each row
    reversed_rows = [row[::-1] for row in matrix]
    
    # Reverse the order of the rows
    # reversed_matrix = reversed_rows[::-1]
    
    return reversed_rows


# Sample matrix
matrix = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

# print(get_diagonals(reverse_matrix(matrix)))


with open('4-ceressearch.txt', 'r') as file:
    # Read the contents of the file 
    content = file.read()
    
    # Reverse the text 
    # reversed_text = text[::-1]
    
    # Horizontal searches
    pattern = r"XMAS"
    pattern1 = r"SAMX"
    # Find all matches 
    hmatches = re.findall(pattern, content)
    hmatches1 = re.findall(pattern1, content)
    # Count the number of matches 
    hcount = len(hmatches)
    hcount1 = len(hmatches1)
    horizontal_count = hcount + hcount1
    print(f"Number of horizontal occurrences: {horizontal_count}")
    
    # Vertical searches
    content_matrix = text_to_matrix(content)
    vertical_content = get_verticals(content_matrix)
    # print(vertical_content)
    # Search verticals
    vcount = 0
    vcount1 = 0
    for vertical in vertical_content:
        vmatches = re.findall(pattern, vertical)
        vmatches1 = re.findall(pattern1, vertical)
        # Count the number of matches 
        vcount += len(vmatches)
        vcount1 += len(vmatches1)
    vertical_count = vcount + vcount1
    print(f"Number of vertical occurrences: {vertical_count}")
    
     # Diagonal searches
    diagonal_content = get_diagonals(content_matrix)
    # print(diagonal_content)
    
    # Search diagonals
    dcount = 0
    dcount1 = 0
    for diagonal in diagonal_content:
        dmatches = re.findall(pattern, diagonal)
        dmatches1 = re.findall(pattern1, diagonal)
        # Count the number of matches 
        dcount += len(dmatches)
        dcount1 += len(dmatches1)
    diagonal_count = dcount + dcount1
    print(f"Number of diagonal occurrences: {diagonal_count}")
    
    # Get reversed diagonal
    reversed = reverse_matrix(content_matrix)
    diagonal_content_reversed = get_diagonals(reversed)
    
    # Search diagonals
    dcountreversed = 0
    dcountreversed1 = 0
    for diagonalrev in diagonal_content_reversed:
        drevmatches = re.findall(pattern, diagonalrev)
        drevmatches1 = re.findall(pattern1, diagonalrev)
        # Count the number of matches 
        dcountreversed += len(drevmatches)
        dcountreversed1 += len(drevmatches1)
    diagonal_reversed_count = dcountreversed + dcountreversed1
    print(f"Number of reversed diagonal occurrences: {diagonal_reversed_count}")
    
    total_occurences = horizontal_count + vertical_count + diagonal_count + diagonal_reversed_count
    print(f"Number of total occurrences: {total_occurences}")
    
    # Part two
    # print(content_matrix)
    
    # Sample 2D matrix 
    matrix2d = [
        ['a', 'b', 'c', 'a'],
        ['d', 'a', 'e', 'f'],
        ['g', 'h', 'a', 'i']
    ]
    
    rows = len(content_matrix)
    cols = len(content_matrix[0])
    
    mascount = 0
    samcount = 0
    mscount = 0
    smcount = 0
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if content_matrix[row][col] == "A" and content_matrix[row-1][col-1] == "M" and content_matrix[row-1][col+1] == "M" and content_matrix[row+1][col-1] == "S" and content_matrix[row+1][col+1] == "S":
                mascount += 1
    
    for row in range(1, rows-1):
        for col in range(1,cols-1):
            if content_matrix[row][col] == "A" and content_matrix[row-1][col-1] == "S" and content_matrix[row-1][col+1] == "S" and content_matrix[row+1][col-1] == "M" and content_matrix[row+1][col+1] == "M":
                samcount += 1
    
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if content_matrix[row][col] == "A" and content_matrix[row-1][col-1] == "M" and content_matrix[row-1][col+1] == "S" and content_matrix[row+1][col-1] == "M" and content_matrix[row+1][col+1] == "S":
                mscount += 1
                
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if content_matrix[row][col] == "A" and content_matrix[row-1][col-1] == "S" and content_matrix[row-1][col+1] == "M" and content_matrix[row+1][col-1] == "S" and content_matrix[row+1][col+1] == "M":
                smcount += 1
    
    totalmas = mascount + samcount + mscount + smcount
    print(f"Number of MAS's: {mascount}")
    print(f"Number of SAM's: {samcount}")
    print(f"Number of MAM's: {mscount}")
    print(f"Number of SAS's: {smcount}")
    print(f"Total number of MAS's: {totalmas}")