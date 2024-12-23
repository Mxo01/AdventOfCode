import networkx as nx


def main():
    lines = read_puzzle()

    graph = create_graph(lines)
    largest_clique = find_largest_clique(graph)

    print(",".join(sorted(largest_clique)))


def create_graph(lines):
    graph = nx.Graph()

    for line in lines:
        first, second = line.split("-")
        graph.add_edge(first, second)

    return graph


def find_largest_clique(graph):
    return max(list(nx.find_cliques(graph)), key=len)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
