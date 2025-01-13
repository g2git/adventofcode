import re

def extract_integers(s):
    return list(map(int, re.findall(r'\d+', s)))


with open("2-cubeconundrum.txt", "r") as file:
    # Dictionary of all games(keys) and their results(values)
    games = {}
    for line in file:
        # Dictionary of plays within a game
        outcomes = {}
        game, result = line.split(": ")
        result = result.split("; ")
        for res in range(len(result)):
            # Dictionary of individual result for each nubered play within a game
            res_dict = {'red': 0, 'green': 0, 'blue': 0}
            for string in result[res].split(","):
                number, color = string.split()
                res_dict[color] = int(number)
            # Store the result(value) of each numbered play(key) in outcomes
            outcomes[res+1] = res_dict
        # Store the outcomes(value) of each game(key) in games
        games[game] = outcomes
    

    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    sum_id = 0
    
    for game_key, values in games.items():
        game_number = extract_integers(game_key)[0]
        for val, colors in values.items():
            if colors["red"] > red_cubes or colors["green"] > green_cubes or colors["blue"] > blue_cubes: break
        else:
            sum_id += game_number 
            continue
            
    print(sum_id)
    
    # Part Two
    power = 0
    for game_key, values in games.items():
        red_max = 0
        green_max = 0
        blue_max = 0
        for val, colors in values.items():
            if colors["red"] > red_max: red_max = colors["red"]
            if colors["green"] > green_max: green_max = colors["green"]
            if colors["blue"] > blue_max: blue_max = colors["blue"]
        # print(f'red_max = {red_max}, green_max = {green_max}, blue_max = {blue_max}')
        power += red_max * green_max * blue_max
        
    print(power)
        
        
