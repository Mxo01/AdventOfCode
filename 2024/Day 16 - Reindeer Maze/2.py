from collections import defaultdict
import heapq

directions = ["E", "S", "W", "N"]
moves = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}


def main():
    maze = read_puzzle()

    source, destination = find_source_and_destination(maze)
    best_paths = a_star_search(maze, source, destination)
    tiles = count_tiles(best_paths)

    print(tiles)


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
    priority_queue = [(heuristic(source, destination), 0, [(sx, sy, "E")])]
    visited = defaultdict(lambda: float("inf"))
    all_paths = []
    shortest_path_cost = float("inf")

    while priority_queue:
        _, cost, path = heapq.heappop(priority_queue)
        x, y, direction = path[-1]
        state = (x, y, direction)

        if cost > shortest_path_cost or cost > visited[state]:
            continue

        if (x, y) == destination:
            if cost < shortest_path_cost:
                shortest_path_cost = cost
                all_paths = [path]
            elif cost == shortest_path_cost:
                all_paths.append(path)

            continue

        visited[state] = cost

        for dir in directions:
            if dir == direction:
                dx, dy = moves[dir]
                nx, ny = x + dx, y + dy

                if maze[nx][ny] != "#":
                    new_path = path + [(nx, ny, dir)]
                    heapq.heappush(
                        priority_queue,
                        (
                            1 + cost + heuristic((nx, ny), destination),
                            1 + cost,
                            new_path,
                        ),
                    )
            else:
                new_path = path + [(x, y, dir)]
                heapq.heappush(
                    priority_queue,
                    (
                        1000 + cost + heuristic((x, y), destination),
                        1000 + cost,
                        new_path,
                    ),
                )

    return all_paths


def heuristic(source, destination):
    sx, sy = source
    dx, dy = destination
    return abs(sx - dx) + abs(sy - dy)


def count_tiles(best_paths):
    return len(set((x, y) for path in best_paths for x, y, _ in path))


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
