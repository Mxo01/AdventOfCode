def main():
    lines = read_puzzle()
    print(sum(1 if char == "(" else -1 for char in lines[0]))

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()