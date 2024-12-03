def main():
    f = open("puzzle.txt", "r")

    multiply_sum = 0
    last_encountered_char = ""
    encountered_digits_before_comma = 0
    encountered_digits_after_comma = 0
    already_encountered_comma = False
    digit_before_comma = ""
    digit_after_comma = ""

    while True:
        char = f.read(1)

        if not char:
            break

        if (
            char != "m"
            and char != "u"
            and char != "l"
            and char != "("
            and char != ")"
            and char != ","
            and not char.isdigit()
        ):
            last_encountered_char = ""
            encountered_digits_before_comma = 0
            encountered_digits_after_comma = 0
            digit_before_comma = ""
            digit_after_comma = ""
            already_encountered_comma = False
            continue

        if char == "m":
            if last_encountered_char != "":
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            last_encountered_char = char
            continue

        if char == "u":
            if last_encountered_char != "m":
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            last_encountered_char = char
            continue

        if char == "l":
            if last_encountered_char != "u":
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            last_encountered_char = char
            continue

        if char == "(":
            if last_encountered_char != "l":
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            last_encountered_char = char
            continue

        if char.isdigit():
            if (
                last_encountered_char != "("
                and last_encountered_char != ","
                and not last_encountered_char.isdigit()
            ):
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            if last_encountered_char == "(":
                encountered_digits_before_comma = 1
                digit_before_comma += char
                last_encountered_char = char
                continue

            if last_encountered_char == ",":
                encountered_digits_after_comma = 1
                digit_after_comma += char
                last_encountered_char = char
                continue

            if last_encountered_char.isdigit():
                if already_encountered_comma:
                    if encountered_digits_after_comma >= 3:
                        last_encountered_char = ""
                        encountered_digits_before_comma = 0
                        encountered_digits_after_comma = 0
                        digit_before_comma = ""
                        digit_after_comma = ""
                        already_encountered_comma = False
                        continue

                    encountered_digits_after_comma += 1
                    digit_after_comma += char
                    last_encountered_char = char
                    continue
                else:
                    if encountered_digits_before_comma >= 3:
                        last_encountered_char = ""
                        encountered_digits_before_comma = 0
                        encountered_digits_after_comma = 0
                        digit_before_comma = ""
                        digit_after_comma = ""
                        already_encountered_comma = False
                        continue

                    encountered_digits_before_comma += 1
                    digit_before_comma += char
                    last_encountered_char = char
                    continue

        if char == ",":
            if not last_encountered_char.isdigit() or already_encountered_comma:
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            last_encountered_char = char
            already_encountered_comma = True
            continue

        if char == ")":
            if not last_encountered_char.isdigit() or not already_encountered_comma:
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            if digit_before_comma == "" or digit_after_comma == "":
                last_encountered_char = ""
                encountered_digits_before_comma = 0
                encountered_digits_after_comma = 0
                digit_before_comma = ""
                digit_after_comma = ""
                already_encountered_comma = False
                continue

            multiply_sum += int(digit_before_comma) * int(digit_after_comma)

            last_encountered_char = ""
            encountered_digits_before_comma = 0
            encountered_digits_after_comma = 0
            digit_before_comma = ""
            digit_after_comma = ""
            already_encountered_comma = False
            continue

    print(multiply_sum)

    f.close()


if __name__ == "__main__":
    main()
