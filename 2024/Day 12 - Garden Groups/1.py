def main():
    lines = read_puzzle()

    rows = len(lines)
    cols = len(lines[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def flood_fill(i, j, plant_type):
        stack = [(i, j)]
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()

            if visited[x][y]:
                continue

            visited[x][y] = True
            area += 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if (
                    nx < 0
                    or nx >= rows
                    or ny < 0
                    or ny >= cols
                    or lines[nx][ny] != plant_type
                ):
                    perimeter += 1
                elif not visited[nx][ny]:
                    stack.append((nx, ny))

        return area * perimeter

    print(
        sum(
            flood_fill(i, j, lines[i][j])
            for i in range(rows)
            for j in range(cols)
            if not visited[i][j]
        )
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
