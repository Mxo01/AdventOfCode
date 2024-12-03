def main():
    f = open("puzzle.txt", "r")

    multiply_sum = 0
    last_encountered_char = ""
    encountered_digits_before_comma = 0
    encountered_digits_after_comma = 0
    already_encountered_comma = False
    digit_before_comma = ""
    digit_after_comma = ""
    can_multiply = ""
    last_encountered_char_for_multiply = ""

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
            and char != "d"
            and char != "o"
            and char != "n"
            and char != "t"
            and char != "'"
            and not char.isdigit()
        ):
            last_encountered_char = ""
            encountered_digits_before_comma = 0
            encountered_digits_after_comma = 0
            digit_before_comma = ""
            digit_after_comma = ""
            already_encountered_comma = False
            continue

        if char == "d":
            last_encountered_char_for_multiply = char
            can_multiply = char
            continue

        if char == "o" and last_encountered_char_for_multiply == "d":
            last_encountered_char_for_multiply = char
            can_multiply += char
            continue

        if char == "n" and last_encountered_char_for_multiply == "o":
            last_encountered_char_for_multiply = char
            can_multiply += char
            continue

        if char == "'" and last_encountered_char_for_multiply == "n":
            last_encountered_char_for_multiply = char
            can_multiply += char
            continue

        if char == "t" and last_encountered_char_for_multiply == "'":
            last_encountered_char_for_multiply = char
            can_multiply += char
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
            if (
                last_encountered_char_for_multiply == "t"
                or last_encountered_char_for_multiply == "o"
            ):
                last_encountered_char_for_multiply = char
                can_multiply += char

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
            if last_encountered_char_for_multiply == "(":
                last_encountered_char_for_multiply = ""
                can_multiply += char
    
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

            if can_multiply == "do()" or can_multiply == "":
                multiply_sum += int(digit_before_comma) * int(digit_after_comma)

            last_encountered_char = ""
            encountered_digits_before_comma = 0
            encountered_digits_after_comma = 0
            digit_before_comma = ""
            digit_after_comma = ""
            already_encountered_comma = False
            continue

    f.close()

    print(multiply_sum)


if __name__ == "__main__":
    main()
