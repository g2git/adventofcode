from collections import deque

# Directions for up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(maze, visited, row, col):
   # Check if the move is inside the grid, not a wall, and not visited
   return (0 <= row < len(maze) and 0 <= col < len(maze[0]) and
         maze[row][col] != '0' and not visited[row][col])

def bfs(maze, start, end):
   rows, cols = len(maze), len(maze[0])
  
   # Queue for BFS, which stores (row, col, path_so_far)
   queue = deque([(start[0], start[1], [])])
   visited = [[False] * cols for _ in range(rows)]
   visited[start[0]][start[1]] = True
  
   while queue:
      row, col, path = queue.popleft()

      # If we've reached the end, return the path
      if (row, col) == end:
         return path + [(row, col)]

      # Explore the neighbors (up, down, left, right)
      for direction in directions:
         new_row, new_col = row + direction[0], col + direction[1]
        
         if is_valid_move(maze, visited, new_row, new_col):
            visited[new_row][new_col] = True
            queue.append((new_row, new_col, path + [(row, col)]))
  
   return None  # If no path is found

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


def convert_maze(maze):
   for i in range(len(maze)):
      for j in range(len(maze[i])):
         # Replace any # value with 1 (wall), and 0 for . and S and E(open space)
         if maze[i][j] == '#':
            maze[i][j] = 1
         else:
            maze[i][j] = 0
   return maze

def replace_element(matrix, old_element, new_element):
   for i, row in enumerate(matrix):
      for j, value in enumerate(row):
         if value == old_element:
            matrix[i][j] = new_element
   return matrix

def find_start_end(maze):
   start = None
   end = None

   # Iterate through the maze to find 'S' (start) and 'E' (end)
   for i in range(len(maze)):
      for j in range(len(maze[i])):
         if maze[i][j] == 'S':
            start = (i, j)
         elif maze[i][j] == 'E':
            end = (i, j)

   return start, end


with open('20-racecondition.txt', 'r') as file:
   maze = []
   for line in file:
      maze.append(list(line.strip()))
   start, end = find_start_end(maze)
   maze = convert_maze(maze)
   # maze = replace_element(maze, "#", 1)
   # maze = replace_element(maze, ".", 0)
   # maze = replace_element(maze, "S", 0)
   # maze = replace_element(maze, "E", 0)

   original_path_length = len(find_all_shortest_paths(maze, start, end)[0])

   tot = 0
   for i in range(1, len(maze)-1):
      for j in range(1, len(maze[i])-1):
         if maze[i][j] == 1:
            maze[i][j] = 0
            path_length = len(find_all_shortest_paths(maze, start, end)[0])
            if path_length > 0:
               path_difference = original_path_length - path_length
               if path_difference >= 100:
                  tot += 1
            maze[i][j] = 1
   print(tot)
   
   
# New approach   
with open('20-racecondition.txt', 'r') as file:
    maze = []
    for line in file:
        maze.append(list(line.strip()))
    rows = len(maze)
    cols = len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                break
        else:
            continue
        break
     
     
    # Distances matrix
    dists = [[-1] * cols for _ in range(rows)]
    dists[r][c] = 0
   
    # Bfs method
    # q = deque([(r,c)])
    # while q:
    #     # Current row and current column
    #     cr, cc = q.popleft()
    #     for nr, nc in [(cr+1,cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
    #         # check if nr, nc are within bounds
    #         if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
    #         if maze[nr][nc] == "#": continue
    #         if dists[nr][nc] != -1: continue
    #         dists[nr][nc] = dists[cr][cc] + 1
    #         q.append((nr, nc))
    # Use this method because there is just one optimal path
    while maze[r][c] != "E":
        # Check all directions
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if nr < 0 or nr >= rows or nc < 0  or nc >= cols: continue
            if maze[nr][nc] == "#": continue
            if dists[nr][nc] != -1: continue
            # For each point save how many steps to that point
            dists[nr][nc] = dists[r][c] + 1
            r, c = nr, nc
    # Get all points for which a cheat to that point saves 100 picoseconds or more
    count = 0
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "#": continue
            for radius in range(2,21):
                # check all points in with manhattan distance equal to radius
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in {(r+dr, c+dc), (r+dr,c-dc), (r-dr,c+dc), (r-dr, c-dc)}:
                        # Check bounds
                        if nr < 0 or nr >= rows or nc < 0  or nc >= cols: continue
                        # if dists[nr][nc] == -1: continue # Works too
                        if maze[nr][nc] == "#": continue
                        if dists[r][c] - dists[nr][nc] >= 100 + radius: count += 1
   
    print(count)
