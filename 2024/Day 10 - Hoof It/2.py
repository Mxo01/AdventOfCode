from collections import deque


def main():
    lines = read_puzzle()

    zeros = find_zeros(lines)
    graph = create_graph(lines)

    print(sum(dfs(graph, zero, lines) for zero in zeros))


def find_zeros(lines):
    return [
        (i, j)
        for i in range(len(lines))
        for j in range(len(lines[i]))
        if lines[i][j] == "0"
    ]


def is_gradual_step(neighbor, node):
    return int(neighbor) - int(node) == 1


def create_graph(lines):
    graph = {}

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            top, bottom, left, right = i - 1, i + 1, j - 1, j + 1

            if top >= 0:
                graph.setdefault((i, j), []).append((top, j))
            if bottom < len(lines):
                graph.setdefault((i, j), []).append((bottom, j))
            if left >= 0:
                graph.setdefault((i, j), []).append((i, left))
            if right < len(lines[i]):
                graph.setdefault((i, j), []).append((i, right))

    return graph


def dfs(graph, source, lines):
    stack = deque([source])
    count = 0

    while stack:
        node = stack.pop()

        if lines[node[0]][node[1]] == "9":
            count += 1

        for neighbor in graph.get(node, []):
            if is_gradual_step(
                lines[neighbor[0]][neighbor[1]], lines[node[0]][node[1]]
            ):
                stack.append(neighbor)

    return count


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
