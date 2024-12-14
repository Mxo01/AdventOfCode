import re
import time

N = 103
M = 101


def main():
    lines = read_puzzle()

    grid = [[0 for _ in range(M)] for _ in range(N)]
    robots = get_robots(lines)
    move_robots(grid, robots)


def get_robots(lines):
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]


def move_robots(grid, robots):
    for i in range(10000):
        for robot in robots:
            x, y, vx, vy = robot

            x = (x + i * vx) % M
            y = (y + i * vy) % N

            grid[y][x] += 1

        has_line_with_20_ones = 0

        for m in range(M):
            if grid[m].count(1) >= 20:
                has_line_with_20_ones += 1

        if has_line_with_20_ones >= 2:
            time.sleep(0.3)
            print(f"\nIteration {i}\n")
            for n in range(N):
                print("".join(list(map(str, grid[n]))).replace("0", ".").replace("1", "1"))

        grid = [[0 for _ in range(M)] for _ in range(N)]


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
