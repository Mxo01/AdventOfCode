ticker_tape_message = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def main():
    lines = read_puzzle()

    aunts = get_aunts(lines)
    aunt = find_aunt(aunts)

    print(aunt)


def get_aunts(lines):
    aunts = []

    for i, line in enumerate(lines):
        parts = list(
            map(lambda x: x.strip(), (",".join(line.split(": ")[1:]).split(",")))
        )

        aunt = {"number": i + 1}

        for i in range(0, len(parts), 2):
            if not parts[i].isdigit():
                aunt[parts[i]] = int(parts[i + 1])

        aunts.append(aunt)

    return aunts


def find_aunt(aunts):
    for aunt in aunts:
        if all(
            (key in ["cats", "trees"] and value > ticker_tape_message[key])
            or (key in ["pomeranians", "goldfish"] and value < ticker_tape_message[key])
            or (
                key not in ["cats", "trees", "pomeranians", "goldfish"]
                and value == ticker_tape_message[key]
            )
            for key, value in aunt.items()
            if key != "number"
        ):
            return aunt["number"]


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
