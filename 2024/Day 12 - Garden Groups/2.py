def main():
    lines = read_puzzle()

    rows = len(lines)
    cols = len(lines[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def flood_fill(i, j, plant_type):
        stack = [(i, j)]
        area = 0
        corners = 0

        while stack:
            x, y = stack.pop()

            if visited[x][y]:
                continue

            visited[x][y] = True
            area += 1

            corners += get_corners(x, y, rows, cols, lines, plant_type)

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and not visited[nx][ny]
                    and lines[nx][ny] == plant_type
                ):
                    stack.append((nx, ny))

        return area * corners

    print(
        sum(
            flood_fill(i, j, lines[i][j])
            for i in range(rows)
            for j in range(cols)
            if not visited[i][j]
        )
    )


def get_corners(x, y, rows, cols, lines, plant_type):
    corners = 0

    if (
        is_top_different_or_outside(y, x - 1, lines, plant_type)
        and is_left_different_or_outside(x, y - 1, lines, plant_type)
    ) or (
        is_top_left_equal(x - 1, y - 1, lines, plant_type)
        and is_top_different_or_outside(y, x - 1, lines, plant_type)
    ):
        corners += 1

    if (
        is_top_different_or_outside(y, x - 1, lines, plant_type)
        and is_right_different_or_outside(x, y + 1, cols, lines, plant_type)
    ) or (
        is_top_right_equal(x - 1, y + 1, cols, lines, plant_type)
        and is_top_different_or_outside(y, x - 1, lines, plant_type)
    ):
        corners += 1

    if (
        is_bottom_different_or_outside(y, x + 1, rows, lines, plant_type)
        and is_left_different_or_outside(x, y - 1, lines, plant_type)
    ) or (
        is_bottom_left_equal(x + 1, y - 1, rows, lines, plant_type)
        and is_bottom_different_or_outside(y, x + 1, rows, lines, plant_type)
    ):
        corners += 1

    if (
        is_bottom_different_or_outside(y, x + 1, rows, lines, plant_type)
        and is_right_different_or_outside(x, y + 1, cols, lines, plant_type)
    ) or (
        is_bottom_right_equal(x + 1, y + 1, rows, cols, lines, plant_type)
        and is_bottom_different_or_outside(y, x + 1, rows, lines, plant_type)
    ):
        corners += 1

    return corners


def is_top_different_or_outside(y, top, lines, plant_type):
    return top < 0 or (lines[top][y] != plant_type)


def is_bottom_different_or_outside(y, bottom, rows, lines, plant_type):
    return bottom >= rows or (lines[bottom][y] != plant_type)


def is_left_different_or_outside(x, left, lines, plant_type):
    return left < 0 or (lines[x][left] != plant_type)


def is_right_different_or_outside(x, right, cols, lines, plant_type):
    return right >= cols or (lines[x][right] != plant_type)


def is_top_left_equal(top, left, lines, plant_type):
    return top >= 0 and left >= 0 and lines[top][left] == plant_type


def is_top_right_equal(top, right, cols, lines, plant_type):
    return top >= 0 and right < cols and lines[top][right] == plant_type


def is_bottom_left_equal(bottom, left, rows, lines, plant_type):
    return bottom < rows and left >= 0 and lines[bottom][left] == plant_type


def is_bottom_right_equal(bottom, right, rows, cols, lines, plant_type):
    return bottom < rows and right < cols and lines[bottom][right] == plant_type


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
