import re

with open('2021/puzzles/day1.txt', 'r') as file:
    puzzle = file.read()

def decode_puzzle(puzzle: str) -> list[int]:
    return [int(num) for num in re.findall(r'\d+', puzzle)]

def part1(puzzle: str) -> int:
    nums: list[int] = decode_puzzle(puzzle)
    return sum([1 for i, num in enumerate(nums) if i > 0 and nums[i - 1] < num])


if __name__ == '__main__':
    print(f'p1: {part1(puzzle)}')