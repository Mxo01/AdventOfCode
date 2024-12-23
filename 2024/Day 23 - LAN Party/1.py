import networkx as nx


def main():
    lines = read_puzzle()

    graph = create_graph(lines)
    cliques = find_cliques(graph)

    print(len(cliques))


def create_graph(lines):
    graph = nx.Graph()

    for line in lines:
        first, second = line.split("-")
        graph.add_edge(first, second)

    return graph


def find_cliques(graph):
    return list(
        map(
            lambda clique: tuple(sorted(clique)),
            filter(
                lambda clique: len(clique) == 3
                and any(computer.startswith("t") for computer in clique),
                nx.enumerate_all_cliques(graph),
            ),
        )
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
