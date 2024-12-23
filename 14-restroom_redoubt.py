import numpy as np
import re
import sys

import numpy as np

def check_consecutive_elements(matrix, num_columns=95):
    # Iterate over each row in the matrix
    for row in matrix:
        for i in range(len(row) - num_columns + 1):  # Ensure there are enough columns left to check
            # Check if the next `num_columns` elements are all equal to the current element
            if np.all(row[i:i+num_columns] == " "):
                return True  # Found 30 consecutive equal elements
    return False  # No such sequence found

def check_consecutive_rows_in_any_column(matrix, num_rows=95):
    # Iterate over all columns
    for col_index in range(matrix.shape[1]):
        # Iterate over the rows to check for 30 consecutive equal elements in the current column
        for i in range(len(matrix) - num_rows + 1):  # Ensure there are enough rows to check
            # Check if the next `num_rows` elements in the specified column are all equal
            if np.all(matrix[i:i+num_rows, col_index] == matrix[i, col_index]):
                print(f"Found {num_rows} consecutive equal elements in column {col_index + 1}!")
                return True  # Found 30 consecutive equal elements
    return False  # No such sequence foun

def check_consecutive_diagonal_elements(matrix, target, num_elements=10):
    rows, cols = matrix.shape

    # Check for main diagonals (top-left to bottom-right)
    for i in range(rows - num_elements + 1):
        for j in range(cols - num_elements + 1):
            # Check the diagonal starting at (i, j)
            diagonal_elements = [matrix[i+k, j+k] for k in range(num_elements)]
            if all(x == target for x in diagonal_elements):  # Check if all elements are equal to target
                print(f"Found {num_elements} consecutive {target} elements in the main diagonal starting at ({i}, {j})!")
                return True

    # Check for anti-diagonals (top-right to bottom-left)
    for i in range(rows - num_elements + 1):
        for j in range(num_elements - 1, cols):
            # Check the anti-diagonal starting at (i, j)
            diagonal_elements = [matrix[i+k, j-k] for k in range(num_elements)]
            if all(x == target for x in diagonal_elements):  # Check if all elements are equal to target
                print(f"Found {num_elements} consecutive {target} elements in the anti-diagonal starting at ({i}, {j})!")
                return True
    return False

with open('14-restroomredoubt.txt', 'r') as file:
    content = [line.split() for line in file]

    new_content = []
    for rows in content:
        ar = []
        for string in rows:
            data = re.findall(r'(-?\d+,-?\d+)', string)
            data = data[0].split(',')
            data = [int(num) for num in data]
            ar.append(data)

        new_content.append(ar)


    space_matrix = [[' '] * 101 for _ in range(103)]
    for i in range(7000, 20000, 1):
        space_matrix = [[' '] * 101 for _ in range(103)]
        for row in new_content:
            col_x = row[0][0]
            row_y = row[0][1]
            col_vel = row[1][0]
            row_vel = row[1][1]
            secs = i

            space_matrix[abs((row_y + row_vel * secs) % len(space_matrix))][abs((col_x + col_vel * secs) % len(space_matrix[0]))] = "X"

            # Define the size of each quadrant
        numpy_matrix = np.array(space_matrix)
        if check_consecutive_diagonal_elements(numpy_matrix, "X"):
            print(i)

    # Save the matrix to a file 
    # Append the matrix to a file with 
    # with open('output.txt', 'ab') as file:
    #     np.savetxt(file, numpy_matrix, fmt='%c')
    
    
    # half_row, half_col = numpy_matrix.shape[0] // 2, numpy_matrix.shape[1] // 2
    # Extract quadrants
    # q1 = numpy_matrix[:half_row, :half_col] # Top-left
    # q2 = numpy_matrix[:half_row, half_col+1:] # Top-right
    # q3 = numpy_matrix[half_row+1:, :half_col] # Bottom-left
    # q4 = numpy_matrix[half_row+1:, half_col+1:] # Bottom-right
]

    # top_left_sum = np.sum(q1)
    # top_right_sum = np.sum(q2)
    # bottom_left_sum = np.sum(q3)
    # bottom_right_sum = np.sum(q4)


    # safety_factor = top_left_sum * top_right_sum * bottom_left_sum * bottom_right_sum
    # print(safety_factor)
