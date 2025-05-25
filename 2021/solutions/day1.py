import re

with open('2021/puzzles/day1.txt', 'r') as file:
    puzzle = file.read()

def decode_puzzle(puzzle: str) -> list[int]:
    return [int(num) for num in re.findall(r'\d+', puzzle)]

def solution(puzzle: str) -> dict[str: int]:
    nums: list[int] = decode_puzzle(puzzle)
    p1: int = sum([1 for i, num in enumerate(nums) if i > 0 and nums[i - 1] < num])
    p2: int = 0
    l,r = 1,3
    while r < len(nums):
        if sum(nums[l:r + 1]) > sum(nums[l - 1:r]):
            p2 += 1
        r += 1
        l += 1
    return {"p1": p1, "p2": p2}



if __name__ == '__main__':
    print(f'solution: {solution(puzzle)}')