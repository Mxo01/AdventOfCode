def main():
    lines = read_puzzle()

    a_registry, b_registry, c_registry, program = parse_puzzle(lines)
    print(run_program(a_registry, b_registry, c_registry, program))


def parse_puzzle(lines):
    a_registry = 0
    b_registry = 0
    c_registry = 0
    program = []

    for line in lines:
        if line.strip() == "":
            continue
        elif "A" in line:
            a_registry = int(line.split(": ")[1])
        elif "B" in line:
            b_registry = int(line.split(": ")[1])
        elif "C" in line:
            c_registry = int(line.split(": ")[1])
        else:
            program = list(map(int, line.split(": ")[1].split(",")))

    return a_registry, b_registry, c_registry, program


def run_program(a_registry, b_registry, c_registry, program):
    output = []
    registries = [a_registry, b_registry, c_registry]
    pointer = 0

    while pointer < len(program):
        first_operand = program[pointer]
        second_operand = program[pointer + 1]

        if first_operand == 0:
            print(f"adv -> A = {registries[0]} (A) // combo({second_operand})")
            second_operand = get_combo_operand(
                second_operand, registries[0], registries[1], registries[2]
            )
            registries[0] = adv_or_bdv_or_cdv(registries[0], second_operand)
        elif first_operand == 1:
            print(f"bxl -> B = {registries[1]} (B) ^ {second_operand}")
            registries[1] = bxl_or_bxc(registries[1], second_operand)
        elif first_operand == 2:
            print(f"bst -> B = combo({second_operand}) % 8")
            second_operand = get_combo_operand(
                second_operand, registries[0], registries[1], registries[2]
            )
            registries[1] = bst_or_out(second_operand)
        elif first_operand == 3:
            print(f"jnz -> {registries[0]} (A)")
            if jnz(registries[0]):
                pointer = second_operand
                continue
        elif first_operand == 4:
            print(f"bxc -> B = {registries[1]} (B) ^ {registries[2]} (C)")
            registries[1] = bxl_or_bxc(registries[1], registries[2])
        elif first_operand == 5:
            print(f"out -> combo({second_operand}) % 8")
            second_operand = get_combo_operand(
                second_operand, registries[0], registries[1], registries[2]
            )
            output.append(str(bst_or_out(second_operand)))
        elif first_operand == 6:
            print(f"bdv -> B = {registries[0]} (A) // combo({second_operand})")
            second_operand = get_combo_operand(
                second_operand, registries[0], registries[1], registries[2]
            )
            registries[1] = adv_or_bdv_or_cdv(registries[0], second_operand)
        elif first_operand == 7:
            print(f"cdv -> C = {registries[0]} (A) // combo({second_operand})")
            second_operand = get_combo_operand(
                second_operand, registries[0], registries[1], registries[2]
            )
            registries[2] = adv_or_bdv_or_cdv(registries[0], second_operand)

        pointer += 2

    return ",".join(output)


def get_combo_operand(op, a_registry, b_registry, c_registry):
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return a_registry
    elif op == 5:
        return b_registry

    return c_registry


def adv_or_bdv_or_cdv(numerator, denominator):
    return numerator // (2**denominator)


def bxl_or_bxc(a, b):
    return a ^ b


def bst_or_out(n):
    return n % 8


def jnz(a_registry):
    return a_registry != 0


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().strip().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
