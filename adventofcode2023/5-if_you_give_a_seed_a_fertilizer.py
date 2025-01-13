with open('5-ifyougiveaseedafertilizer.txt', 'r') as file:
    seeds, *blocks = file.read().split('\n\n')
    seeds = list(map(int, seeds.split(': ')[1].split()))

for block in blocks:
    block = block.split(':')[1].strip().splitlines()
    ranges = []
    for line in block:
        ranges.append(list(map(int, line.split())))
    new = []
    for seed in seeds:
        for destination, source, r in ranges:
            if seed in range(source, source + r):
                new.append(seed - source + destination)
                break
        else:
            new.append(seed)
    seeds = new
print(f'minimum seeds = {min(seeds)}')