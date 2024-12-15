directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def main():
    lines = read_puzzle()

    grid, moves, robot_pos = parse_puzzle(lines)
    move_robot(grid, moves, robot_pos)
    boxes_gps_coordinates = get_boxes_gps_coordinates(grid)

    print(boxes_gps_coordinates)


def parse_puzzle(lines):
    grid = []
    moves = ""
    grid_readed = False
    robot_pos = None

    for i, line in enumerate(lines):
        if line.strip() == "":
            grid_readed = True
            continue

        if not grid_readed:

            if "@" in line:
                robot_pos = (i, line.index("@"))

            grid.append(list(line))

        if grid_readed:
            moves += line

    return grid, list(moves), robot_pos


def move_robot(grid, moves, robot_pos):
    for move in moves:
        i, j = robot_pos
        delta_i, delta_j = directions[move]
        new_i, new_j = i + delta_i, j + delta_j

        if grid[new_i][new_j] == ".":
            grid[i][j] = "."
            grid[new_i][new_j] = "@"
            robot_pos = (new_i, new_j)

        if grid[new_i][new_j] == "#":
            continue

        if grid[new_i][new_j] == "O":
            can_push, first_free_space_pos = can_push_box(grid, new_i, new_j, move)

            if can_push:
                free_space_i, free_space_j = first_free_space_pos
                grid[i][j] = "."
                grid[new_i][new_j] = "@"
                grid[free_space_i][free_space_j] = "O"
                robot_pos = (new_i, new_j)
            else:
                continue
        
def can_push_box(grid, box_i, box_j, move):
    i, j = box_i, box_j
    delta_i, delta_j = directions[move]
    new_i, new_j = i + delta_i, j + delta_j

    while grid[new_i][new_j] != "#":
        if grid[new_i][new_j] == ".":
            return True, (new_i, new_j)
        else:
            i, j = new_i, new_j
            new_i, new_j = i + delta_i, j + delta_j

    return False, None


def get_boxes_gps_coordinates(grid):
    return sum(
        100 * i + j
        for i in range(len(grid))
        for j in range(len(grid[i]))
        if grid[i][j] == "O"
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
