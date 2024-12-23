def main():
    starting_secret_numbers = list(map(int, read_puzzle()))

    secret_numbers = generate_secret_numbers(starting_secret_numbers)

    print(sum(secret_numbers))


def generate_secret_numbers(starting_secret_numbers):
    secret_numbers = []

    for secret_number in starting_secret_numbers:
        next_secret_number = secret_number

        for _ in range(2000):
            next_secret_number = generate_next_secret_number(next_secret_number)

        secret_numbers.append(next_secret_number)

    return secret_numbers


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
