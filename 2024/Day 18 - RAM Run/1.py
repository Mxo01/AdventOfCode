import heapq

grid_size = 71
allowed_bytes = 1024
directions = ["E", "S", "W", "N"]
moves = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}


def main():
    lines = read_puzzle()

    bytes_positions = get_bytes_positions(lines)
    grid = create_grid(bytes_positions)
    steps = a_star_search(grid)

    print(steps)


def get_bytes_positions(lines):
    return [tuple(map(int, line.split(","))) for line in lines][:allowed_bytes]


def create_grid(bytes_positions):
    return [
        ["#" if (y, x) in bytes_positions else "." for y in range(grid_size)]
        for x in range(grid_size)
    ]


def a_star_search(grid, source=(0, 0), destination=(grid_size - 1, grid_size - 1)):
    sx, sy = source
    priority_queue = [(heuristic(source, destination), (sx, sy, 0))]
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
                and grid[nx][ny] != "#"
            ):
                heapq.heappush(
                    priority_queue,
                    (
                        1 + cost + heuristic((nx, ny), destination),
                        (nx, ny, cost + 1),
                    ),
                )

    return -1


def heuristic(source, destination):
    sx, sy = source
    dx, dy = destination
    return abs(sx - dx) + abs(sy - dy)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
