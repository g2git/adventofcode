import heapq
import networkx as nx

# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dx, dy)
# direction_names = ['up', 'down', 'left', 'right']

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

# Find all shortest paths
def create_maze_graph(maze):
    G = nx.grid_2d_graph(len(maze), len(maze[0]))
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 1:  # 1 represents a wall
                G.remove_node((x, y))
    return G

def find_all_shortest_paths(maze, start, goal):
    G = create_maze_graph(maze)
    try:
        all_paths = list(nx.all_shortest_paths(G, source=start, target=goal))
        return all_paths
    except nx.NetworkXNoPath:
        return None


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
    
    return sum(1 for count in position_count.values() if count >= 1 )

def unique_points_count(paths):
    # Use a set to keep track of unique coordinates
    unique_coordinates = set()
    # Iterate through each path and add coordinates to the set
    for path in paths:
        for coordinate in path:
            unique_coordinates.add(coordinate)
    # Count the number of unique coordinates
    unique_count = len(unique_coordinates)
    return unique_count


# Define the directions and their corresponding costs
directions = {
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1),
    'up': (-1, 0)
}
rotation_cost = 1000
move_cost = 1

# Function to get the next direction after a rotation
def rotate(current_direction, rotation):
    directions_list = list(directions.keys())
    current_index = directions_list.index(current_direction)
    if rotation == 'left':
        return directions_list[(current_index - 1) % 4]
    elif rotation == 'right':
        return directions_list[(current_index + 1) % 4]

# Function to add edges to the graph
def add_edges(G, maze, start_direction):
    rows, cols = len(maze), len(maze[0])
    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == 0:
                for direction in directions:
                    dx, dy = directions[direction]
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                        G.add_edge((x, y, direction), (nx, ny, direction), weight=move_cost)
                    new_direction_left = rotate(direction, 'left')
                    new_direction_right = rotate(direction, 'right')
                    G.add_edge((x, y, direction), (x, y, new_direction_left), weight=rotation_cost)
                    G.add_edge((x, y, direction), (x, y, new_direction_right), weight=rotation_cost)

# Function to find all paths with the lowest score
def find_paths(maze, start, end):
    G = nx.DiGraph()
    add_edges(G, maze, 'right')
    start_node = (start[0], start[1], 'right')
    end_nodes = [(end[0], end[1], direction) for direction in directions]
    paths = []
    min_score = float('inf')

    for end_node in end_nodes:
        for path in nx.all_shortest_paths(G, source=start_node, target=end_node, weight='weight'):
            score = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            if score < min_score:
                min_score = score
                paths = [path]
            elif score == min_score:
                paths.append(path)

    return paths




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

    # lowest_score = find_path_with_lowest_score(maze, start, end)
    # print(lowest_score)
    

    
    # Find all paths with the lowest score
    paths = find_paths(maze, start, end)
    all_paths = []

    for path in paths:
        adj_path = []
        for step in path:
            adj_path.append(step[:2])
        all_paths.append(adj_path)
    
    multiple_occurrences = count_positions_in_multiple_paths(all_paths)
    print(multiple_occurrences)