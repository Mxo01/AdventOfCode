import re


def main():
    lines = read_puzzle()

    reindeers = get_reindeers(lines)
    distance_traveled = get_distance_traveled(reindeers)

    print(max(distance_traveled))


def get_distance_traveled(reindeers):
    distance_traveled = []

    for reindeer in reindeers:
        speed, fly_time, rest_time = reindeer
        is_flying = True
        distance = 0
        time_spent_flying = 0
        time_spent_resting = 0

        for _ in range(2503):
            if time_spent_flying == fly_time:
                is_flying = False
                time_spent_flying = 0

            if time_spent_resting == rest_time:
                is_flying = True
                time_spent_resting = 0

            if is_flying:
                distance += speed
                time_spent_flying += 1

            if not is_flying:
                time_spent_resting += 1

        distance_traveled.append(distance)

    return distance_traveled


def get_reindeers(lines):
    return [get_reindeer_values(line) for line in lines]


def get_reindeer_values(line):
    return list(map(int, re.findall(r"\d+", line)))


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
