

dir_map: dict = {
    "forward": (1, 0),
    "down": (0, 1),
    "up": (0, -1)
}

with open('2021/puzzles/day2.txt') as file:
    puzzle: str = file.read()

def solution(puzzle: str):
    directions: list[tuple[tuple[int], int]] = [(dir_map[l.split(' ')[0]], int(l.split(' ')[1]) ) for l in puzzle.split('\n')]
    # part 1:
    cur_pos: tuple[int] = (0, 0)
    for d in directions:
        cur_pos = (cur_pos[0] + d[0][0] * d[1], cur_pos[1] + d[0][1] * d[1])
    print(f'position: {cur_pos}')
    solution: dict = {"p1": abs(cur_pos[0] * cur_pos[1])}
    # part 2:
    cur_pos: tuple[int] = (0, 0)
    aim: int = 0

    for d in directions:
        if d[0] == (1, 0):
            cur_pos = (cur_pos[0] + d[1], (aim * d[1]) + cur_pos[1])
        else:
            aim += d[1] if d[0] == (0, 1) else -1 * d[1]
    print(f'position: {cur_pos}')
    solution["p2"] = cur_pos[0] * cur_pos[1]
    print(f'solution: {solution}')


if __name__ == '__main__':
    solution(puzzle) 