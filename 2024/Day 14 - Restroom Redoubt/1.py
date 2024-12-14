import re

N = 103
M = 101


def main():
    lines = read_puzzle()

    grid = [[0 for _ in range(M)] for _ in range(N)]
    move_robots(grid, lines)
    safety_factor = count_safety_factor(grid)

    print(safety_factor)


def move_robots(grid, lines):
    for line in lines:
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        grid[(y + 100 * vy) % N][(x + 100 * vx) % M] += 1


def count_safety_factor(grid):
    return (
        sum(grid[i][j] for i in range(N // 2) for j in range(M // 2))
        * sum(grid[i][j] for i in range(N // 2) for j in range(M // 2 + 1, M))
        * sum(grid[i][j] for i in range(N // 2 + 1, N) for j in range(M // 2))
        * sum(grid[i][j] for i in range(N // 2 + 1, N) for j in range(M // 2 + 1, M))
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()