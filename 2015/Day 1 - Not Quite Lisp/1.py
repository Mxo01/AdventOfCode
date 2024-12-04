def main():
    lines = read_puzzle()

    floor = sum(1 if char == "(" else -1 for char in lines[0])

    print(floor)

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()