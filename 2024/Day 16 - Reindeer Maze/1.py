import heapq

directions = ["E", "S", "W", "N"]
moves = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}


def main():
    maze = read_puzzle()

    source, destination = find_source_and_destination(maze)
    lowest_points = a_star_search(maze, source, destination)

    print(lowest_points)


def find_source_and_destination(maze):
    source = None
    destination = None

    for x, row in enumerate(maze):
        for y, cell in enumerate(row):
            if cell == "S":
                source = (x, y)
            elif cell == "E":
                destination = (x, y)

    return source, destination


def a_star_search(maze, source, destination):
    sx, sy = source
    priority_queue = [(heuristic(source, destination), (sx, sy, "E", 0))]
    visited = set()

    while priority_queue:
        _, (x, y, direction, cost) = heapq.heappop(priority_queue)

        if (x, y) == destination:
            return cost

        if (x, y, direction) in visited:
            continue

        visited.add((x, y, direction))

        for dir in directions:
            if dir == direction:
                dx, dy = moves[dir]
                nx, ny = x + dx, y + dy

                if maze[nx][ny] != "#":
                    heapq.heappush(
                        priority_queue,
                        (
                            1 + cost + heuristic((nx, ny), destination),
                            (nx, ny, dir, cost + 1),
                        ),
                    )
            else:
                heapq.heappush(
                    priority_queue,
                    (
                        1000 + cost + heuristic((x, y), destination),
                        (x, y, dir, cost + 1000),
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
