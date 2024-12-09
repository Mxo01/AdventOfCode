import re


def main():
    password = [char for char in read_puzzle()[0]]

    while True:
        password = increment_password(password)

        if is_valid_password(password) or has_only_a(password):
            break

    print("".join(password))


def increment_password(password):
    should_break = False
    i = -1

    while not should_break and abs(i) <= len(password):
        should_break = password[i] != "z"
        next_char = ord(password[i]) + (1 if password[i] != "z" else -(122 - 97))
        password[i] = chr(next_char if next_char <= 122 else 97)

        i -= 1

    return password


def has_only_a(password):
    return all(list(map(lambda char: char == "a", password)))


def is_valid_password(password):
    return (
        has_increasing_three(password)
        and has_two_pairs(password)
        and not has_iol(password)
    )


def has_increasing_three(password):
    return any(
        ord(password[i + 1]) - ord(password[i]) == 1
        and ord(password[i + 2]) - ord(password[i + 1]) == 1
        for i in range(0, len(password) - 2)
    )


def has_two_pairs(password):
    return len(set(re.findall(r"(.)\1", "".join(password)))) >= 2


def has_iol(password):
    return "i" in password or "o" in password or "l" in password


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
