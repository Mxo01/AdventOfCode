def main():
    lines = read_puzzle()

    visited = set()
    visited.add((0, 0))
    x1, y1, x2, y2 = 0, 0, 0, 0
    should_move_santa = False

    for line in lines:
        for direction in line:
            should_move_santa = not should_move_santa

            if should_move_santa:
                x1 += 1 if direction == ">" else -1 if direction == "<" else 0
                y1 += 1 if direction == "^" else -1 if direction == "v" else 0
            else:
                x2 += 1 if direction == ">" else -1 if direction == "<" else 0
                y2 += 1 if direction == "^" else -1 if direction == "v" else 0

            visited.add((x1, y1) if should_move_santa else (x2, y2))

    print(len(visited))


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
