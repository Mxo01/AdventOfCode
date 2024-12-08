def main():
    lines = read_puzzle()
    print(
        sum(
            len('"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"') - len(line)
            for line in lines
        )
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
