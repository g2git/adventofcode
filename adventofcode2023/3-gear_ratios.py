with open('3-gearratios.txt', 'r') as file:
    grid = file.read().splitlines()

integer_coords = set()
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if grid[r][c] == '.' or grid[r][c].isdigit(): continue 
        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[r]) or not grid[cr][cc].isdigit(): continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                integer_coords.add((cr, cc))


part_numbers = 0
for r,c in integer_coords:
    # Integer string
    string = grid[r][c]
    while c+1 < len(grid[r]) and grid[r][c+1].isdigit():
        string += grid[r][c+1]
        c += 1
    part_numbers += int(string)

print(part_numbers)

# Part Two
gear_ratios = []
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if grid[r][c] != '*': continue
        nums = set()
        for cr in [r-1, r, r+1]:
            for cc in [c-1, c, c+1]:
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[r]) or not grid[cr][cc].isdigit(): continue
                while cc > 0 and grid[cr][cc-1].isdigit():
                    cc -= 1
                nums.add((cr,cc))
        if len(nums) == 2: gear_ratios.append(nums)


gear_total = 0
for coords in gear_ratios:
    coords_product = 1
    for cor in coords:
        (r,c) = cor
        string = grid[r][c]
        while c+1 < len(grid[r]) and grid[r][c+1].isdigit():
            string += grid[r][c+1]
            c += 1
        coords_product *= int(string)
    gear_total += coords_product
print(gear_total)