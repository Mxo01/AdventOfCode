import re


def main():
    lines = read_puzzle()

    reindeers = get_reindeers(lines)
    winning_reindeer = get_winning_reindeer(reindeers)

    print(winning_reindeer)


def get_winning_reindeer(reindeers):
    points = {i: 0 for i in range(len(reindeers))}
    distance_traveled = [(0, True, 0, 0) for _ in range(len(reindeers))]

    for _ in range(2503):
        for i, reindeer in enumerate(reindeers):
            speed, fly_time, rest_time = reindeer
            distance, is_flying, time_spent_flying, time_spent_resting = distance_traveled[i]

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

            distance_traveled[i] = distance, is_flying, time_spent_flying, time_spent_resting

        leader = max(distance_traveled, key=lambda r: r[0])[0]
        
        for i, distance in enumerate(distance_traveled):
            if distance[0] == leader:
                points[i] += 1

    return max(points.values())


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
