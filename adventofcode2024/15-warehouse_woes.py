import sys
import copy


def next_position(coords, direction):
        # Up position
    if direction == "^":
        return [coords[0]-1, coords[1]]
        # Right position
    if direction == ">":
        return [coords[0], coords[1]+1]
        # Down position
    if direction == "v":
        return [coords[0]+1, coords[1]]
        # Left position
    if direction == "<":
        return [coords[0], coords[1]-1]
    
def next_char(matrix, coords, direction):
    next_pos = next_position(coords, direction)
    return matrix[next_pos[0]][next_pos[1]]

def make_move(matrix, current_pos, direction):
    next_pos = next_position(current_pos, direction)
    if next_char(matrix, current_pos, direction) == "#":
        return matrix
    if next_char(matrix, current_pos, direction) == ".":
        matrix[next_pos[0]][next_pos[1]] = matrix[current_pos[0]][current_pos[1]]
        matrix[current_pos[0]][current_pos[1]] = "."
        return matrix
    if next_char(matrix, current_pos, direction) == "O":
        matrix = make_move(matrix, next_pos, direction)
        if next_char(matrix, current_pos, direction) == ".":
            matrix = make_move(matrix, current_pos, direction)
            return matrix
        else:
            return matrix
    
    
def find_element_position(matrix, element):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == element:
                return [i, j]
    return None
    
def find_all_coordinates(matrix, element):
    coordinates = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == element: coordinates.append([i, j]) 
    return coordinates

def create_new_map(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            if value == '#':
                new_row.append(value)
                new_row.append(value)
            if value == 'O':
                new_row.append('[')
                new_row.append(']')
            if value == '.':
                new_row.append(value)
                new_row.append(value)
            if value == '@':
                new_row.append('@')
                new_row.append('.')
        new_matrix.append(new_row)
    return new_matrix

def new_make_move(matrix, current_pos, direction):
    next_pos = next_position(current_pos, direction)
    if next_char(matrix, current_pos, direction) == "#":
        return matrix
    if next_char(matrix, current_pos, direction) == ".":
        matrix[next_pos[0]][next_pos[1]] = matrix[current_pos[0]][current_pos[1]]
        matrix[current_pos[0]][current_pos[1]] = "."
        return matrix
    if next_char(matrix, current_pos, direction) == "[":
        matrix = move_brackets(matrix, next_pos, [next_pos[0], next_pos[1]+1], direction)
        if next_char(matrix, current_pos, direction) == ".":
            matrix = new_make_move(matrix, current_pos, direction)
            return matrix
        else:
            return matrix
    if next_char(matrix, current_pos, direction) == "]":
        matrix = move_brackets(matrix, [next_pos[0], next_pos[1]-1], next_pos, direction)
        if next_char(matrix, current_pos, direction) == ".":
            matrix = new_make_move(matrix, current_pos, direction)
            return matrix
        else:
            return matrix

def move_brackets(matrix, leftbracket, rightbracket, direction):
    if matrix[leftbracket[0]][leftbracket[1]] == "[" and matrix[rightbracket[0]][rightbracket[1]] == "]":
        # Move brackets up
        if direction == "^":
            next_pos_above_left = next_position(leftbracket, direction)
            next_pos_above_right = next_position(rightbracket, direction)
            # # Above
            if next_char(matrix, leftbracket, direction) == "#" or next_char(matrix, rightbracket, direction) == "#":
                return matrix
            # .. Above
            if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                matrix[next_pos_above_left[0]][next_pos_above_left[1]] = "["
                matrix[next_pos_above_right[0]][next_pos_above_right[1]] = "]"
                matrix[leftbracket[0]][leftbracket[1]] = "."
                matrix[rightbracket[0]][rightbracket[1]] = "."
                return matrix
            # [] Above
            if next_char(matrix, leftbracket, direction) == "[" and next_char(matrix, rightbracket, direction) == "]":
                matrix = move_brackets(matrix, next_pos_above_left, next_pos_above_right, direction)
                if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix
            # ]. Above
            if next_char(matrix, leftbracket, direction) == "]" and next_char(matrix, rightbracket, direction) == ".":
                matrix = move_brackets(matrix, [next_pos_above_left[0], next_pos_above_left[1]-1],next_pos_above_left, direction)
                if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix
            # .[ Above
            if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == "[":
                matrix = move_brackets(matrix, next_pos_above_right, [next_pos_above_right[0], next_pos_above_right[1]+1], direction)
                if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix
            # ][ Above
            if next_char(matrix, leftbracket, direction) == "]" and next_char(matrix, rightbracket, direction) == "[":
                # Deep copy of the matrix 
                deep_copy = copy.deepcopy(matrix)
                deep_copy = move_brackets(deep_copy, [next_pos_above_left[0], next_pos_above_left[1]-1], next_pos_above_left, direction)
                deep_copy = move_brackets(deep_copy, next_pos_above_right, [next_pos_above_right[0], next_pos_above_right[1]+1], direction)
                if next_char(deep_copy, leftbracket, direction) == "." and next_char(deep_copy, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, [next_pos_above_left[0], next_pos_above_left[1]-1], next_pos_above_left, direction)
                    matrix = move_brackets(matrix, next_pos_above_right, [next_pos_above_right[0], next_pos_above_right[1]+1], direction)
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix
                
                
        # Move brackets down
        if direction == "v":
            next_pos_below_left = next_position(leftbracket, direction)
            next_pos_below_right = next_position(rightbracket, direction)
            # # Below
            if next_char(matrix, leftbracket, direction) == "#" or next_char(matrix, rightbracket, direction) == "#":
                return matrix
            # .. Below
            if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                matrix[next_pos_below_left[0]][next_pos_below_left[1]] = "["
                matrix[next_pos_below_right[0]][next_pos_below_right[1]] = "]"
                matrix[leftbracket[0]][leftbracket[1]] = "."
                matrix[rightbracket[0]][rightbracket[1]] = "."
                return matrix
            # [] Below
            if next_char(matrix, leftbracket, direction) == "[" and next_char(matrix, rightbracket, direction) == "]":
                matrix = move_brackets(matrix, next_pos_below_left, next_pos_below_right, direction)
                if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix
            # ]. Below
            if next_char(matrix, leftbracket, direction) == "]" and next_char(matrix, rightbracket, direction) == ".":
                matrix = move_brackets(matrix, [next_pos_below_left[0], next_pos_below_left[1]-1],next_pos_below_left, direction)
                if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix
            # .[ Below
            if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == "[":
                matrix = move_brackets(matrix, next_pos_below_right, [next_pos_below_right[0], next_pos_below_right[1]+1], direction)
                if next_char(matrix, leftbracket, direction) == "." and next_char(matrix, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix
            # ][ Below
            if next_char(matrix, leftbracket, direction) == "]" and next_char(matrix, rightbracket, direction) == "[":
                # Deep copy of the matrix 
                deep_copy = copy.deepcopy(matrix)
                deep_copy = move_brackets(deep_copy, [next_pos_below_left[0], next_pos_below_left[1]-1],next_pos_below_left, direction)
                deep_copy = move_brackets(deep_copy, next_pos_below_right, [next_pos_below_right[0], next_pos_below_right[1]+1], direction)
                if next_char(deep_copy, leftbracket, direction) == "." and next_char(deep_copy, rightbracket, direction) == ".":
                    matrix = move_brackets(matrix, [next_pos_below_left[0], next_pos_below_left[1]-1],next_pos_below_left, direction)
                    matrix = move_brackets(matrix, next_pos_below_right, [next_pos_below_right[0], next_pos_below_right[1]+1], direction)
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix

            
        # Move brackets left
        if direction == "<":
            next_pos = next_position(leftbracket, direction)
            if next_char(matrix, leftbracket, direction) == "#":
                return matrix
            if next_char(matrix, leftbracket, direction) == ".":
                matrix[next_pos[0]][next_pos[1]] = "["
                matrix[leftbracket[0]][leftbracket[1]] = "]"
                matrix[rightbracket[0]][rightbracket[1]] = "."
                return matrix
            if next_char(matrix, leftbracket, direction) == "]":
                matrix = move_brackets(matrix, [next_pos[0], next_pos[1]-1], next_pos, direction)
                if next_char(matrix, leftbracket, direction) == ".": 
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix   
           
        # Move brackets right
        if direction == ">":
            next_pos = next_position(rightbracket, direction)
            if next_char(matrix, rightbracket, direction) == "#":
                return matrix
            if next_char(matrix, rightbracket, direction) == ".":
                matrix[next_pos[0]][next_pos[1]] = "]"
                matrix[rightbracket[0]][rightbracket[1]] = "["
                matrix[leftbracket[0]][leftbracket[1]] = "."
                return matrix
            if next_char(matrix, rightbracket, direction) == "[":
                matrix = move_brackets(matrix, next_pos, [next_pos[0], next_pos[1]+1], direction)
                if next_char(matrix, rightbracket, direction) == ".": 
                    matrix = move_brackets(matrix, leftbracket, rightbracket, direction)
                    return matrix
                else:
                    return matrix    
    else:
        print(f'Error at brackets {leftbracket} and {rightbracket}')
        sys.exit()


with open('15-warehousewoes.txt', 'r') as file:
    warehouse_map = []
    for line in file:
        warehouse_map.append(list(line.strip()))
    
    new_warehouse_map = create_new_map(warehouse_map)

with open('15-warehousewoes-movements.txt', 'r') as file:
    content = file.read()
    moves = list(content.replace('\n', ''))
    for mov in moves:
        robot_pos = find_element_position(warehouse_map, "@")
        warehouse_map = make_move(warehouse_map, robot_pos, mov)
        
    # boxes_coords = find_all_coordinates(warehouse_map, "O")
    # sum_boxes = sum([100*a[0] + a[1] for a in boxes_coords])
    
    for mov in moves:
        robot_pos = find_element_position(new_warehouse_map, "@")
        new_warehouse_map = new_make_move(new_warehouse_map, robot_pos, mov)
    
    boxes_coords = find_all_coordinates(new_warehouse_map, "[")
    sum_boxes = sum([100*a[0] + a[1] for a in boxes_coords])
    print(sum_boxes)