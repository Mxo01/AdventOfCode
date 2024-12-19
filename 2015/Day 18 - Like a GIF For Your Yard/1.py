directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
steps = 100
grid_size = 100


def main():
    lines = read_puzzle()

    grid = [list(line) for line in lines]
    lights_on = get_lights_on(grid, steps)

    print(lights_on)


def get_lights_on(grid, steps):

    for _ in range(steps):
        lights_on = 0
        new_grid = [row.copy() for row in grid]

        for row in range(grid_size):
            for col in range(grid_size):
                neighbours_on = get_neighbours_on(grid, row, col)

                if grid[row][col] == "#":
                    if neighbours_on < 2 or neighbours_on > 3:
                        new_grid[row][col] = "."
                    else:
                        lights_on += 1
                else:
                    if neighbours_on == 3:
                        new_grid[row][col] = "#"
                        lights_on += 1

        grid = new_grid

    return lights_on


def get_neighbours_on(grid, row, col):
    return sum(
        1
        for dx, dy in directions
        if 0 <= row + dx < grid_size
        and 0 <= col + dy < grid_size
        and grid[row + dx][col + dy] == "#"
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
