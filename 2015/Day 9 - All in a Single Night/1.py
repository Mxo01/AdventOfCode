from itertools import permutations


def main():
    lines = read_puzzle()

    graph = create_graph(lines)
    min_cost = float("inf")

    for city in graph:
        cost = find_shortest_path(graph, city)

        if cost < min_cost:
            min_cost = cost

    print(min_cost)


def create_graph(lines):
    graph = {}

    for line in lines:
        city1, _, city2, _, distance = line.split(" ")

        if city1 not in graph:
            graph[city1] = {}

        if city2 not in graph:
            graph[city2] = {}

        graph[city1][city2] = int(distance)
        graph[city2][city1] = int(distance)

    return graph


def find_shortest_path(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)

    all_permutations = permutations(nodes)
    min_cost = float("inf")

    for perm in all_permutations:
        current_cost = 0
        current_path = [start] + list(perm)

        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]

        if current_cost < min_cost:
            min_cost = current_cost

    return min_cost


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()


{
    "London": {"Dublin": 464, "Belfast": 518},
    "Dublin": {"London": 464, "Belfast": 141},
    "Belfast": {"London": 518, "Dublin": 141},
}
