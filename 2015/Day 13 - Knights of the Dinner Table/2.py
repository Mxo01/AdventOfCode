from itertools import permutations


def main():
    lines = read_puzzle()
    print(get_max_happiness(get_guests_happiness(lines)))


def get_guests_happiness(lines):
    people = {}

    for line in lines:
        splitted = line.split(" ")
        person_1 = splitted[0]
        person_2 = splitted[-1][:-1]
        happiness = int(splitted[3]) if splitted[2] == "gain" else -int(splitted[3])

        people.setdefault(person_1, {}).update({person_2: happiness})
        people.setdefault(person_1, {}).update({"Me": 0})

    people.update({"Me": {person: 0 for person in people.keys()}})

    return people


def get_max_happiness(guests_happiness):
    return max(
        calculate_happiness(guests_happiness, permutation)
        for permutation in permutations(guests_happiness.keys())
    )


def calculate_happiness(people, permutation):
    happiness = 0
    n = len(permutation)

    for i in range(n):
        guest_1 = permutation[i]
        guest_2 = permutation[(i + 1) % n]

        happiness += people[guest_1][guest_2] + people[guest_2][guest_1]

    return happiness


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
