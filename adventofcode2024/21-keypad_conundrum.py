from collections import deque, defaultdict
from itertools import product
from functools import cache
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
    
    
instructions = ['341A','083A','802A','973A','780A']
# tot = 0
# for inst in instructions:
#     num = extract_integer_part(inst)
#     ss = shortest_string(rob)
#     rob1 = all_press_buttons(maze2, ss)
#     ss = shortest_string(rob1)
#     rob2 = all_press_buttons(maze2, ss)
 
#     short_string = min(rob2, key=len) 
#     length_of_shortest_string = len(short_string)
    # tot += num * length_of_shortest_string
# print(tot)


# New approach
def compute_seqs(keypad):
    # Create a dictionary for all keypad buttons as keys and their coordinate positions as values
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r, c)
    # Create a dictionary with the tuple of two keypad buttons (x, y) as keys and the minimum moves needed to go from one button to the other
    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            # Create a list of all shortest moves from button x to button y and store the list in seqs as value for key (x, y)
            possibilities = []
            optimal_lentgth = float('inf')
            q = deque([(pos[x], "")])
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in [(r-1, c, "^"), (r+1, c, "v"), (r, c+1, ">"), (r, c-1, "<")]:
                    if nr < 0 or nr >= len(keypad) or nc < 0 or nc >= len(keypad[0]): continue
                    if keypad[nr][nc] is None: continue
                    
                    # If destination is reached
                    if keypad[nr][nc] == y:
                        # Algorithm will find all shortest paths first,
                        # if the pathlength is larger than the shortest path then break out of the loop because the algorithm has finished finding all the shortest paths.
                        if optimal_lentgth < len(moves+nm): break
                        optimal_lentgth = len(moves+nm)
                        possibilities.append(moves+nm+"A")
                    else:
                        # Append the new position and the moves required to get there to the queue list
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break
            seqs[(x,y)] = possibilities
    return seqs 

def solve(string, keypad):
    seqs = compute_seqs(keypad)
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    # Return Cartesian product from all possible combinations
    # *options makes all elements in options array a seperate input 
    return ["".join(x) for x in product(*options)]

number_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]
direction_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

number_sequences = compute_seqs(number_keypad)
direction_sequences = compute_seqs(direction_keypad)
direction_seqs_len = {key: len(value[0]) for key, value in direction_sequences.items()}

# Store all function outputs in memory to avoid repetitive calculations using cache
@cache
def compute_length(seq, depth=25):
    if depth == 1:
        return sum(direction_seqs_len[x, y] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        # For all x to y i.e the entire sequence, determine which subsequence of button x to button y is the shortest and add it to length
        length += min(compute_length(subseq, depth-1) for subseq in direction_sequences[(x, y)])
    return length

total = 0
for ins in instructions:
    # Get all shortest moves possible for the string
    inputs = solve(ins, number_keypad)
    # Get the shortest from the inputs moves at depth 25
    min_len = min(map(compute_length, inputs))
    # Calculate total
    total += min_len * int(ins[:-1])
    
print(total)