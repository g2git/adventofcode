import heapq
import sys
from collections import deque, defaultdict
import json

# Increase the recursion limit 
#  sys.setrecursionlimit(5000)

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dx, dy)
direction_names = ['up', 'down', 'left', 'right']

def find_path_with_lowest_score(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    # Initialize the score grid with infinite values for each direction
    inf = float('inf')
    score_grid = [[[inf] * 4 for _ in range(cols)] for _ in range(rows)]  # [row][col][direction]

    # Priority queue (min-heap): (cost, x, y, direction)
    pq = []
    
    # Start point: we assume we start from the 'right' direction (index 3)
    start_direction = 3  # Facing right
    heapq.heappush(pq, (0, start[0], start[1], start_direction))  # Start with 0 cost at the start point
    score_grid[start[0]][start[1]][start_direction] = 0

    while pq:
        score, x, y, dir = heapq.heappop(pq)
        
        # If we've reached the end, return the score
        if (x, y) == end:
            return score
        
        # Explore 4 possible directions
        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0:
                # Calculate new cost
                new_score = score + 1  # cost of moving to the next cell
                
                # If direction changes, add rotation cost
                if dir != i:
                    new_score += 1000
                
                # If the new path is better, update the score and push to queue
                if new_score < score_grid[new_x][new_y][i]:
                    score_grid[new_x][new_y][i] = new_score
                    heapq.heappush(pq, (new_score, new_x, new_y, i))
    
    # If no path is found, return -1
    return -1


def save_state(paths, filename='paths.json'):
    with open(filename, 'w') as file:
        json.dump(paths, file)

def load_state(filename='paths.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def find_paths(maze, start, end, path=[], paths=[], save_interval=1):
    x, y = start
    if start == end:
        paths.append(path + [end])
        if len(paths) % save_interval == 0:
            save_state(paths)
        return paths
    
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == 1:
        return paths
    
    maze[x][y] = 1  # Mark the cell as visited
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_start = (x + dx, y + dy)
        find_paths(maze, new_start, end, path + [start], paths, save_interval)
    
    maze[x][y] = 0  # Unmark the cell
    return paths



def find_element_position(matrix, element):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == element:
                return (i, j)
    return None

def replace_element(matrix, old_element, new_element):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == old_element:
                matrix[i][j] = new_element
    return matrix


def count_positions_in_multiple_paths(paths):
    position_count = {}
    for path in paths:
        for position in path:
            if position in position_count:
                position_count[position] += 1
            else:
                position_count[position] = 1
    
    return sum(1 for count in position_count.values() if count > 1)

sys.setrecursionlimit(10**6)
# sys.setrecursionlimit(3000)
count = 0

def find_all_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # This will store all the paths from start to finish
    all_paths = []
    
    # Helper function for DFS with backtracking
    def dfs(x, y, path, visited):
        # If we reach the destination, add the path to the list of all paths
        global count
        count += 1
        print('hello', x, y, count)
        if (x, y) == end:
            # print('helloooooooooooooooooooo', x, y, count)
            all_paths.append(path[:])  # Append a copy of the current path
            print(all_paths)
            sys.exit()
            return
        
        # Explore all 4 directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if the new position is within bounds and is not a wall
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0:
                new_pos = (new_x, new_y)
                
                # If the new position hasn't been visited yet, visit it
                if new_pos not in visited:
                    visited.add(new_pos)  # Mark the position as visited
                    path.append(new_pos)  # Add the new position to the path
                    
                    # Recursively explore the new position
                    dfs(new_x, new_y, path, visited)
                    
                    # Backtrack: remove the last position from the path and visited set
                    visited.remove(new_pos)
                    path.pop()


    # Initialize the visited set and start DFS
    visited = set()
    visited.add(start)
    dfs(start[0], start[1], [start], visited)
    
    return all_paths


# Directions: up, down, left, right
# DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_all_paths(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_list = []  # Priority queue for A*
    closed_list = set()  # To store explored nodes
    all_paths = []  # To store all paths
    
    # A* specific data: g (cost to reach node), h (heuristic), f (g + h)
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start, []))  # (f, g, current position, path)
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        # If we reach the goal, store the path
        if current == goal:
            all_paths.append(path + [current])
            continue  # Continue to find other paths
        
        # Explore neighbors
        for dx, dy in DIRECTIONS:
            nx, ny = current[0] + dx, current[1] + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:  # Valid and walkable
                new_position = (nx, ny)
                
                # Avoid revisiting nodes that are already in the closed list
                if new_position not in closed_list:
                    closed_list.add(new_position)
                    new_path = path + [current]
                    new_g = g + 1  # Each move has a cost of 1
                    new_f = new_g + heuristic(new_position, goal)  # f = g + h
                    
                    # Push the new state to the priority queue
                    heapq.heappush(open_list, (new_f, new_g, new_position, new_path))
    
    return all_paths

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs_all_paths(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])  # (current position, current path)
    all_paths = []  # To store all paths
    
    visited = set()  # To prevent revisiting the same cell in the current path
    visited.add(start)
    
    while queue:
        current, path = queue.popleft()
        
        # If we reach the goal, store the path
        if current == goal:
            all_paths.append(path)
            continue  # Continue exploring other potential paths
        
        # Explore neighbors (up, down, left, right)
        for dx, dy in DIRECTIONS:
            nx, ny = current[0] + dx, current[1] + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:  # Valid move
                new_position = (nx, ny)
                
                # Add the new position to the path if it's not visited
                if new_position not in visited:
                    new_path = path + [new_position]
                    queue.append((new_position, new_path))  # Add to queue for further exploration
                    
                    # Add the new position to the visited set to avoid revisiting it in this path
                    visited.add(new_position)
    
    return all_paths


def find_all_best_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS queue: stores (current_position, current_path)
    queue = deque([(start, [start])])
    
    # Dictionary to track all paths to a particular node (key: node, value: list of paths)
    paths_to_node = defaultdict(list)
    
    # Set to track visited nodes to avoid revisiting
    visited = set()
    visited.add(start)
    
    # Track shortest path length
    shortest_path_length = float('inf')
    
    while queue:
        (x, y), path = queue.popleft()
        
        # If we reach the end node
        if (x, y) == end:
            # If this path is shorter than the known shortest path, reset the paths
            if len(path) < shortest_path_length:
                shortest_path_length = len(path)
                paths_to_node.clear()  # Clear previous longer paths
                paths_to_node[(x, y)] = [path]
            # If the path is of the same length as the shortest, add it to the list of paths
            elif len(path) == shortest_path_length:
                paths_to_node[(x, y)].append(path)
            continue
        
        # Explore all 4 directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0:
                new_pos = (new_x, new_y)
                if new_pos not in visited:
                    visited.add(new_pos)
                    new_path = path + [new_pos]
                    queue.append(((new_x, new_y), new_path))
    
    # Return all shortest paths
    return paths_to_node[end]

def count_multiple_occurrences(paths):
    position_count = {}
    
    # Count the occurrences of each position across all paths
    for path in paths:
        for position in path:
            if position in position_count:
                position_count[position] += 1
            else:
                position_count[position] = 1
    
    # Count how many positions appear in more than one path
    multiple_occurrences = sum(1 for count in position_count.values() if count > 1)
    
    return multiple_occurrences

def find_non_repetitive_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    all_paths = []
    
    # Helper function for DFS traversal
    def dfs(x, y, path, visited):
        # If we reach the end, add the current path to the all_paths list
        if (x, y) == end:
            all_paths.append(path[:])  # Add a copy of the path
            return
        
        # Mark the current position as visited
        visited.add((x, y))

        # Explore 4 possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if the new position is within bounds, not a wall, and not visited
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                path.append((new_x, new_y))  # Add the new position to the path
                dfs(new_x, new_y, path, visited)  # Recurse to the next position
                path.pop()  # Backtrack by removing the last position
        
        # Unmark the current position as visited before returning (backtrack)
        visited.remove((x, y))

    # Start DFS from the start position
    dfs(start[0], start[1], [start], set())
    
    return all_paths


def find_all_shortest_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    all_paths = []  # This will store all the shortest paths
    queue = deque([(start, [start])])  # Queue stores tuples of (current_position, current_path)
    visited = set()  # Set to track visited nodes to avoid revisiting during BFS
    visited.add(start)
    shortest_path_length = float('inf')  # To track the length of the shortest path found

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (x, y), path = queue.popleft()

        # If we reach the end node
        if (x, y) == end:
            # If this path length is shorter than the known shortest path, reset all paths
            if len(path) < shortest_path_length:
                shortest_path_length = len(path)
                all_paths = [path]  # Start new list for shortest paths
            # If the path length is the same as the shortest, add it to all_paths
            elif len(path) == shortest_path_length:
                all_paths.append(path)
            continue

        # Explore all 4 directions (up, down, left, right)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0:
                new_pos = (new_x, new_y)
                if new_pos not in visited:
                    visited.add(new_pos)  # Mark as visited
                    queue.append(((new_x, new_y), path + [(new_x, new_y)]))  # Add to queue with updated path

    return all_paths



with open('16-reindeermaze.txt', 'r') as file:
    maze = []
    for line in file:
        maze.append(list(line.strip()))
    
    maze = replace_element(maze, "#", 1)
    maze = replace_element(maze, ".", 0)
    start = find_element_position(maze, "S")
    end = find_element_position(maze, "E")
    maze = replace_element(maze, "S", 0)
    maze = replace_element(maze, "E", 0)

    # print(maze)
    # sys.exit()
    # lowest_score = find_path_with_lowest_score(maze, start, end)
    # print(lowest_score)
    
    paths = bfs_all_paths(maze, start, end)
    for path in paths:
        print(path)
    multiple_occurrences = count_multiple_occurrences(paths)
    print(multiple_occurrences)