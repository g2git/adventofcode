# from collections import deque
from collections import deque, defaultdict
import sys

maze1= [
    ['#', '#', '#', '#', '#'],
    ['#', '7', '8', '9', '#'],
    ['#', '4', '5', '6', '#'],
    ['#', '1', '2', '3', '#'],
    ['#', '#', '0', 'A', '#'],
    ['#', '#', '#', '#', '#']
]

maze2= [
    ['#', '#', '#', '#', '#'],
    ['#', '#', '^', 'A', '#'],
    ['#', '<', 'v', '>', '#'],
    ['#', '#', '#', '#', '#']
]


# Function to find the shortest path in a maze
def shortest_path_in_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    
    # Directions: (row_change, col_change, direction_symbol)
    directions = [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]
    
    # BFS initialization
    queue = deque([(start[0], start[1])])  # Queue to explore the maze
    visited = [[False] * cols for _ in range(rows)]  # Track visited cells
    visited[start[0]][start[1]] = True
    parent = {}  # To store parent position for backtracking
    
    # Perform BFS to find the shortest path
    while queue:
        x, y = queue.popleft()
        
        # If we reach the end, we stop
        if (x, y) == end:
            break
        
        # Explore all possible directions (up, right, down, left)
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maze[nx][ny] != '#':
                visited[nx][ny] = True
                parent[(nx, ny)] = (x, y, direction)  # Store parent and direction
                queue.append((nx, ny))
    
    # Backtrack to get the path
    path = []
    current = end
    while current != start:
        x, y = current
        prev_x, prev_y, direction = parent[current]
        path.append(direction)  # Store the direction
        current = (prev_x, prev_y)
    
    # Reverse the path since we backtracked from end to start
    path.reverse()
    
    # Return the path as a string of directions
    return ''.join(path)+'A'


# Function to find all possible shortest paths in a maze
def all_shortest_paths_in_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    
    # Directions: (row_change, col_change, direction_symbol)
    directions = [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]
    
    # BFS initialization
    queue = deque([(start[0], start[1])])  # Queue to explore the maze
    visited = [[False] * cols for _ in range(rows)]  # Track visited cells
    visited[start[0]][start[1]] = True
    parent = defaultdict(list)  # Store all parent positions for each cell
    path_length = [[float('inf')] * cols for _ in range(rows)]  # Store shortest path length
    
    # Initial position has path length 0
    path_length[start[0]][start[1]] = 0

    # Perform BFS to explore all shortest paths
    while queue:
        x, y = queue.popleft()
        
        # Explore all possible directions (up, right, down, left)
        for dx, dy, direction in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is valid and not a wall
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                
                # If we have found a shorter path to (nx, ny), update and enqueue it
                if path_length[nx][ny] > path_length[x][y] + 1:
                    path_length[nx][ny] = path_length[x][y] + 1
                    parent[(nx, ny)] = [(x, y, direction)]  # Start a new list of parents
                    queue.append((nx, ny))
                
                # If we find another path of the same length, add it as another parent
                elif path_length[nx][ny] == path_length[x][y] + 1:
                    parent[(nx, ny)].append((x, y, direction))

    # Backtrack to find all paths
    def backtrack(x, y):
        # If we reach the start position, return an empty list
        if (x, y) == start:
            return [[]]  # Start has no direction to move to
        
        # Collect all possible paths for the current position
        paths = []
        for px, py, direction in parent[(x, y)]:
            subpaths = backtrack(px, py)  # Recursively backtrack
            for subpath in subpaths:
                paths.append([direction] + subpath)
        
        return paths

    # Find all paths by backtracking from the end
    all_paths = backtrack(end[0], end[1])

    # Convert paths to strings
    return [''.join(path[::-1])+'A' for path in all_paths]

# Example usage:

# Maze representation
# S = Start, E = End, # = Wall, . = Open space
# maze = [
#     "#########",
#     "#S......#",
#     "#.######.",
#     "#.......#",
#     "#.#####.#",
#     "#.......E",
#     "#########"
# ]

# start = (3, 1)  # Starting position (row, col)
# end = (5, 7)    # Ending position (row, col)

# Call the function
# result = all_shortest_paths_in_maze(maze, start, end)
# for path in result:
#     print(path)  # Output will be all possible shortest paths



def find_element(matrix, element):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)
    return None

def press_buttons(maze, buttons):
    path = ''
    buttons = 'A' + buttons
    for i in range(len(buttons)-1):
        start = find_element(maze, buttons[i])
        end = find_element(maze, buttons[i+1])
        path += shortest_path_in_maze(maze, start, end)
    return path

def all_press_buttons(maze, all_buttons):
    all_paths = []
    for buttons in all_buttons:
        paths = ['']
        buttons = 'A' + buttons
        for i in range(len(buttons)-1):
            new_paths = []
            start = find_element(maze, buttons[i])
            end = find_element(maze, buttons[i+1])
            for p in paths:
                sps = [p + aspim for aspim in all_shortest_paths_in_maze(maze, start, end)]
                for sp in sps:
                    new_paths.append(sp)
            paths = new_paths
        for path in paths:
            all_paths.append(path)
    return all_paths
    
def extract_integer_part(s):
    # Extract digits from the string
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else None

def shortest_string(array): 
    min_length = min(len(s) for s in array)
    # Collect all strings of the shortest length
    shortest_strings = [s for s in array if len(s) == min_length]
    return shortest_strings

def multiple_robots_press_buttons(maze1, maze2, instructions):
    tot = 0
    for inst in instructions:
        print(inst)
        num = extract_integer_part(inst)
        rob = all_press_buttons(maze1, [inst])
        for i in range(25):
            print(i)
            ss = shortest_string(rob)
            rob = all_press_buttons(maze2, ss)
    
        short_string = min(rob, key=len) 
        length_of_shortest_string = len(short_string)
        tot += num * length_of_shortest_string
    return tot

def buttons_recursion(maze1, maze2, instructions, iterations, first=True):
    arr = []
    paths =['']
    path = '' 
    # print(iterations)
    if iterations > 0:
        # print(instructions)
        # instructions = shortest_string(instructions)
        for index, ins in enumerate(instructions):
            ins = 'A' + ins
            if first:
                for i in range(len(ins)-1):
                    start = find_element(maze1, ins[i])
                    end = find_element(maze1, ins[i+1])
                    pressed_buttons = buttons_recursion(maze1, maze2, all_shortest_paths_in_maze(maze1, start, end), iterations-1, False)
                # pressed_buttons = buttons_recursion(maze1, maze2, all_press_buttons(maze1, instructions), iterations-1, False)
                    # new_paths = []
                    # for p in paths:
                    #     sp = [p + pb for pb in pressed_buttons]
                    #     for s in sp:
                    #         print(s)
                    #         new_paths.append(s)
                    # paths = new_paths
                    path += min(pressed_buttons, key=len)
                    # print(path)
                # print(pressed_buttons)
                return(path)
                # return min(paths, key=len)

            else:
                for i in range(len(ins)-1):
                    start = find_element(maze2, ins[i])
                    end = find_element(maze2, ins[i+1])
                    pressed_buttons = buttons_recursion(maze1, maze2, all_shortest_paths_in_maze(maze2, start, end), iterations-1, False)
                    pressed_buttons = min(pressed_buttons, key=len)
                    new_paths = []
                    for p in paths:
                        sp = [p + pb for pb in pressed_buttons]
                        for s in sp:
                            new_paths.append(s)
                    paths = new_paths
                    paths = shortest_string(paths)
                    # paths = list(set(paths))
                    print(paths)
                    # print(pressed_buttons)
                    # sys.exit()
                # instructions = shortest_string(instructions)
                # pressed_buttons = buttons_recursion(maze1, maze2, all_press_buttons(maze2, instructions), iterations-1, False)
                    # paths = for p in pressed_buttons]
                for p in paths:   
                    arr.append(p)
                # arr.append(pressed_buttons)
                if index == len(instructions) - 1:
                    return shortest_string(arr)
                # return pressed_buttons
            
    else:
        # print(instructions)
        return shortest_string(instructions)
   
    
# Example usage:

# Maze representation
# S = Start, E = End, # = Wall, . = Open space
# maze = [
#     "#########",
#     "#.......#",
#     "#.######.",
#     "#...S...#",
#     "#.#####.#",
#     "#.......E",
#     "#########"
# ]

# start = (5, 8)  # Starting position (row, col)
# end = (3, 4)    # Ending position (row, col)

# # Call the function
# result = shortest_path_in_maze(maze, start, end)
# print(result)  # Output will be a string of directions
instructions = ['341A','083A','802A','973A','780A']
tot = 0
for inst in instructions:
    num = extract_integer_part(inst)
    # print(inst)
    # print(buttons_recursion(maze1, maze2, [inst], 3))
    # print(inst)
    # length_of_shortest_string = len(buttons_recursion(maze1, maze2, [inst], 3))
#     ss = shortest_string(rob)
#     rob1 = all_press_buttons(maze2, ss)
#     ss = shortest_string(rob1)
#     rob2 = all_press_buttons(maze2, ss)
#     print(rob2)
 
#     short_string = min(rob2, key=len) 
#     length_of_shortest_string = len(short_string)
    # tot += num * length_of_shortest_string
# print(tot)
print(buttons_recursion(maze1, maze2, ['973A'], 3))
# print(len(['<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'][0]))