def main():
    lines = read_puzzle()

    floor = 0

    for line in lines:
        for i in range(len(line)):
            floor += 1 if line[i] == "(" else -1
            
            if floor < 0:
                print(i + 1)
                return

def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()