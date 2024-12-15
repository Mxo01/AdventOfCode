import os
import time


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
            grid.append(
                list(
                    line.replace("#", "##")
                    .replace("O", "[]")
                    .replace(".", "..")
                    .replace("@", "@.")
                )
            )

            if "@" in grid[i]:
                robot_pos = (i, grid[i].index("@"))

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

        if grid[new_i][new_j] in ["[", "]"]:
            if move in ["<", ">"]:
                can_push, first_free_space_pos = can_push_box_horizontal(
                    grid, new_i, new_j, move
                )

                if can_push:
                    _, free_space_j = first_free_space_pos
                    grid[i] = grid[i][:free_space_j] + grid[i][free_space_j + 1 :]
                    grid[i].insert(j, ".")
                    robot_pos = (new_i, new_j)
                else:
                    continue

            if move in ["^", "v"]:
                if grid[new_i][new_j] == "[":
                    opening = (new_i, new_j)
                    closing = (new_i, new_j + 1)
                else:
                    opening = (new_i, new_j - 1)
                    closing = (new_i, new_j)

                can_push = can_push_box_vertical(grid, opening, closing, move)

                if can_push:
                    push_box_vertical(grid, opening, closing, move)

                    grid[i][j] = "."
                    grid[new_i][new_j] = "@"
                    robot_pos = (new_i, new_j)


def can_push_box_vertical(grid, opening, closing, move):
    opening_i, opening_j = opening
    closing_i, closing_j = closing
    delta_i, delta_j = directions[move]
    new_left_i, new_left_j = opening_i + delta_i, opening_j + delta_j
    new_right_i, new_right_j = closing_i + delta_i, closing_j + delta_j
    can_push_left, can_push_right = True, True

    if grid[new_left_i][new_left_j] == "#" or grid[new_right_i][new_right_j] == "#":
        return False

    if grid[new_left_i][new_left_j] == "." and grid[new_right_i][new_right_j] == ".":
        return True

    if grid[new_left_i][new_left_j] in ["[", "]"]:
        if grid[new_left_i][new_left_j] == "[":
            new_opening_left = (new_left_i, new_left_j)
            new_closing_left = (new_left_i, new_left_j + 1)
        else:
            new_opening_left = (new_left_i, new_left_j - 1)
            new_closing_left = (new_left_i, new_left_j)

        can_push_left = can_push_box_vertical(
            grid, new_opening_left, new_closing_left, move
        )

    if grid[new_right_i][new_right_j] in ["[", "]"]:
        if grid[new_right_i][new_right_j] == "[":
            new_opening_right = (new_right_i, new_right_j)
            new_closing_right = (new_right_i, new_right_j + 1)
        else:
            new_opening_right = (new_right_i, new_right_j - 1)
            new_closing_right = (new_right_i, new_right_j)

        can_push_right = can_push_box_vertical(
            grid, new_opening_right, new_closing_right, move
        )

    return can_push_left and can_push_right


def push_box_vertical(grid, opening, closing, move):
    opening_i, opening_j = opening
    closing_i, closing_j = closing
    delta_i, delta_j = directions[move]
    new_left_i, new_left_j = opening_i + delta_i, opening_j + delta_j
    new_right_i, new_right_j = closing_i + delta_i, closing_j + delta_j

    if grid[new_left_i][new_left_j] == "." and grid[new_right_i][new_right_j] == ".":
        grid[new_left_i][new_left_j] = "["
        grid[new_right_i][new_right_j] = "]"
        grid[opening_i][opening_j] = "."
        grid[closing_i][closing_j] = "."

        return

    if grid[new_left_i][new_left_j] in ["[", "]"]:
        if grid[new_left_i][new_left_j] == "[":
            new_opening = (new_left_i, new_left_j)
            new_closing = (new_left_i, new_left_j + 1)
        else:
            new_opening = (new_left_i, new_left_j - 1)
            new_closing = (new_left_i, new_left_j)

        push_box_vertical(grid, new_opening, new_closing, move)

    if grid[new_right_i][new_right_j] in ["[", "]"]:
        if grid[new_right_i][new_right_j] == "[":
            new_opening = (new_right_i, new_right_j)
            new_closing = (new_right_i, new_right_j + 1)
        else:
            new_opening = (new_right_i, new_right_j - 1)
            new_closing = (new_right_i, new_right_j)

        push_box_vertical(grid, new_opening, new_closing, move)

    grid[new_left_i][new_left_j] = "["
    grid[new_right_i][new_right_j] = "]"
    grid[opening_i][opening_j] = "."
    grid[closing_i][closing_j] = "."


def can_push_box_horizontal(grid, box_i, box_j, move):
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
        if grid[i][j] == "["
    )


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
