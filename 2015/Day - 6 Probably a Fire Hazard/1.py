def main():
    lines = read_puzzle()
    grid = [[False for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        from_coordinate, to_coordinate = [
            coordinate.strip() for coordinate in line.split("through")
        ]
        from_start, from_end = [
            int(index) for index in from_coordinate.split(" ")[-1].split(",")
        ]
        to_start, to_end = [int(index) for index in to_coordinate.split(",")]
        on, off = "turn on" in line, "turn off" in line

        for i in range(from_start, to_start + 1):
            for j in range(from_end, to_end + 1):
                grid[i][j] = True if on else False if off else not grid[i][j]

    print(sum([row.count(True) for row in grid]))


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
