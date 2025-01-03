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
   # print(maze)
   # original_path_length = len(bfs(maze,start,end))
   # print(original_path_length)
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
