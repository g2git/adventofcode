import functools

def parse_input(filename: str) -> list[int]:
    with open(filename, 'r') as f:
        line = f.readline()

    stones = list(map(int, line.strip().split(' ')))

    return stones

@functools.cache
def go_deep(stone: int, depth_remaining: int) -> int:
    if depth_remaining == 0:
        return 1

    if stone == 0:
        return go_deep(1, depth_remaining - 1)
    # If the stone is engraved with a number that has an even number of digits,
    # split into two stones, by string
    elif len(str(stone)) % 2 == 0:
        orig_stone = stone
        orig_stone_str = str(orig_stone)
        left_stone_str = orig_stone_str[0:len(orig_stone_str) // 2]
        right_stone_str = orig_stone_str[len(orig_stone_str) // 2:]
        left_stone = int(left_stone_str)
        right_stone = int(right_stone_str)
        return go_deep(left_stone, depth_remaining - 1) + go_deep(right_stone, depth_remaining - 1)
    # If none of the other rules apply, the stone is replaced by a stone multiplied by 2024
    else:
        return go_deep(stone * 2024, depth_remaining - 1)

def go_deep_stones(stones: list[int], depth: int) -> int:
    count = 0
    for stone in stones:
        count += go_deep(stone, depth)
    return count

def part1():
    stones = parse_input('input.txt')
    print(f"25 deep: {go_deep_stones(stones, 25)}")

if __name__ == '__main__':
    for depth in range(5, 155, 1):
        stones = parse_input('input.txt')
        print(f"{depth} deep: {go_deep_stones(stones, depth)}")