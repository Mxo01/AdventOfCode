def main():
    line = read_puzzle()[0]
    print(len(look_and_say(line, 50)))


def look_and_say(line, iterations):
    if iterations == 0:
        return line
    
    updated_line = []
    substr = ""

    for i in range(len(line) - 1):
        substr += line[i]

        if line[i] != line[i + 1]:
            updated_line.append(substr)
            substr = ""

    updated_line.append(line[-1])
    updated_line = "".join(list(map(lambda group: str(len(group)) + group[0], updated_line)))

    return look_and_say(updated_line, iterations - 1)


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
