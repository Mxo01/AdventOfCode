import heapq

directions = ["E", "S", "W", "N"]
moves = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}
cheat_moves = {"E": (0, 2), "S": (2, 0), "W": (0, -2), "N": (-2, 0)}


def main():
    maze = read_puzzle()

    source, destination = create_grid(maze)
    path = a_star_search(maze, source, destination)
    cheats = find_cheats(maze, path)

    print(cheats)


def create_grid(maze):
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
    priority_queue = [(heuristic(source, destination), (sx, sy, 0))]
    visited = set()
    maze_size = len(maze)
    parent_map = {}

    while priority_queue:
        _, (x, y, cost) = heapq.heappop(priority_queue)

        if (x, y) == destination:
            path = []
            current = (x, y)

            while current:
                path.append(current)
                current = parent_map.get(current)

            return path[::-1]

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dir in directions:
            dx, dy = moves[dir]
            nx, ny = x + dx, y + dy

            if (
                0 <= nx <= maze_size - 1
                and 0 <= ny <= maze_size - 1
                and maze[nx][ny] != "#"
                and (nx, ny) not in visited
            ):
                heapq.heappush(
                    priority_queue,
                    (
                        1 + cost + heuristic((nx, ny), destination),
                        (nx, ny, cost + 1),
                    ),
                )

                if (nx, ny) not in parent_map:
                    parent_map[(nx, ny)] = (x, y)

    return []


def heuristic(source, destination):
    sx, sy = source
    dx, dy = destination
    return abs(sx - dx) + abs(sy - dy)


def find_cheats(maze, path):
    possible_cheats = 0
    maze_size = len(maze)
    path_length = len(path) - 1
    cell_distance_from_end = {cell: path_length - i for i, cell in enumerate(path)}

    for cell in path:
        x, y = cell

        for dir in directions:
            dx, dy = cheat_moves[dir]
            nx, ny = x + dx, y + dy

            if (
                0 <= nx <= maze_size - 1
                and 0 <= ny <= maze_size - 1
                and (nx, ny) in path
                and cell_distance_from_end[(nx, ny)] - cell_distance_from_end[(x, y)]
                > 100
            ):
                possible_cheats += 1

    return possible_cheats


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
