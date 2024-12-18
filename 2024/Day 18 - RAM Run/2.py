import heapq

grid_size = 71
allowed_bytes = 1024
directions = ["E", "S", "W", "N"]
moves = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}


def main():
    lines = read_puzzle()

    bytes_positions = get_bytes_positions(lines)
    coordinates = get_coordinates(bytes_positions)

    print(coordinates)


def get_bytes_positions(lines):
    return [tuple(map(int, line.split(","))) for line in lines]


def get_coordinates(bytes_positions):
    for incremental_allowed_bytes in range(allowed_bytes, len(bytes_positions)):
        grid = create_grid(bytes_positions, incremental_allowed_bytes)
        cost = a_star_search(grid)

        if cost == -1:
            return bytes_positions[incremental_allowed_bytes - 1]

    return None


def create_grid(bytes_positions, allowed_bytes):
    return [
        [
            "#" if (y, x) in bytes_positions[:allowed_bytes] else "."
            for y in range(grid_size)
        ]
        for x in range(grid_size)
    ]


def a_star_search(maze, source=(0, 0), destination=(grid_size - 1, grid_size - 1)):
    sx, sy = source
    priority_queue = [(heuristic(sx, sy, destination), (sx, sy, 0))]
    visited = set()

    while priority_queue:
        _, (x, y, cost) = heapq.heappop(priority_queue)

        if (x, y) == destination:
            return cost

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dir in directions:
            dx, dy = moves[dir]
            nx, ny = x + dx, y + dy

            if (
                0 <= nx <= grid_size - 1
                and 0 <= ny <= grid_size - 1
                and maze[nx][ny] != "#"
            ):
                heapq.heappush(
                    priority_queue,
                    (
                        1 + cost + heuristic(nx, ny, destination),
                        (nx, ny, cost + 1),
                    ),
                )

    return -1


def heuristic(row, col, destination):
    dx, dy = destination
    return abs(row - dx) + abs(col - dy)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
