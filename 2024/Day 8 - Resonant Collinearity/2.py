def main():
    lines = read_puzzle()

    antennas = {}
    antinodes = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j].isdigit() or lines[i][j].isalpha():
                antennas.setdefault(lines[i][j], []).append((i, j))
                antinodes.add((i, j))

    antennas = dict(filter(lambda antenna: len(antenna[1]) > 1, antennas.items()))

    for positions in antennas.values():
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                current_position = positions[i]
                next_position = positions[j]

                distance = (
                    current_position[0] - next_position[0],
                    current_position[1] - next_position[1],
                )

                first_antinode = (
                    current_position[0] + distance[0],
                    current_position[1] + distance[1],
                )
                second_antinode = (
                    next_position[0] - distance[0],
                    next_position[1] - distance[1],
                )

                while not is_node_out_of_bounds(
                    first_antinode, lines
                ) or not is_node_out_of_bounds(second_antinode, lines):
                    if not is_node_out_of_bounds(first_antinode, lines):
                        antinodes.add(first_antinode)
                        first_antinode = (
                            first_antinode[0] + distance[0],
                            first_antinode[1] + distance[1],
                        )

                    if not is_node_out_of_bounds(second_antinode, lines):
                        antinodes.add(second_antinode)
                        second_antinode = (
                            second_antinode[0] - distance[0],
                            second_antinode[1] - distance[1],
                        )

    print(len(antinodes))


def is_node_out_of_bounds(node, lines):
    return (
        node[0] < 0 or node[0] >= len(lines[0]) or node[1] < 0 or node[1] >= len(lines)
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
