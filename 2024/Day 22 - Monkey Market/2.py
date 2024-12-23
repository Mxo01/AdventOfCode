from collections import defaultdict


def main():
    starting_secret_numbers = list(map(int, read_puzzle()))

    most_bananas_overall = get_most_banans_overall(starting_secret_numbers)

    print(most_bananas_overall)


def get_most_banans_overall(starting_secret_numbers):
    sequences = defaultdict(int)

    for secret_number in starting_secret_numbers:
        sequence = []
        current_secret_number = secret_number
        visited = set()

        for _ in range(2000):
            next_secret_number = generate_next_secret_number(current_secret_number)
            current_secret_number_last_digit = current_secret_number % 10
            next_secret_number_last_digit = next_secret_number % 10
            change = next_secret_number_last_digit - current_secret_number_last_digit

            sequence.append(change)

            if len(sequence) == 4:
                if tuple(sequence) not in visited:
                    sequences[tuple(sequence)] += next_secret_number_last_digit
                    visited.add(tuple(sequence))

                sequence.pop(0)

            current_secret_number = next_secret_number

    return max(sequences.values())


def generate_next_secret_number(secret_number):
    secret_number = prune(mix(secret_number * 64, secret_number))
    secret_number = prune(mix(secret_number // 32, secret_number))
    secret_number = prune(mix(secret_number * 2048, secret_number))

    return secret_number


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
