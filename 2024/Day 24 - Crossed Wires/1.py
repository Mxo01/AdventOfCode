import re


def main():
    lines = read_puzzle()

    result = run_circuit(lines)

    print(result)


def run_circuit(lines):
    wires, instructions = read_instructions(lines)

    filtered_circuit = {
        wire: evaluate(wire, wires, instructions, {})
        for wire in sorted(instructions, reverse=True)
        if wire.startswith("z")
    }

    return to_decimal(filtered_circuit)


def read_instructions(lines):
    wires, instructions = {}, {}

    wires_readed = False

    for line in lines:
        if line.strip() == "":
            wires_readed = True
            continue
        elif not wires_readed:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        else:
            parsed = parse_instruction(line)
            wire = parsed[3]
            instructions[wire] = parsed[:-1]

    return wires, instructions


def parse_instruction(instruction):
    if "AND" in instruction:
        m = re.match(r"(\w+) AND (\w+) -> (\w+)", instruction)
        return ("AND", m.group(1), m.group(2), m.group(3))
    elif "XOR" in instruction:
        m = re.match(r"(\w+) XOR (\w+) -> (\w+)", instruction)
        return ("XOR", m.group(1), m.group(2), m.group(3))
    else:
        m = re.match(r"(\w+) OR (\w+) -> (\w+)", instruction)
        return ("OR", m.group(1), m.group(2), m.group(3))


def evaluate(wire, wires, instructions, cache):
    if wire.isdigit():
        return int(wire)

    if wire in cache:
        return cache[wire]

    if wire in wires:
        return wires[wire]

    operation, wire_1, wire_2 = instructions[wire]

    if operation == "AND":
        result = evaluate(wire_1, wires, instructions, cache) & evaluate(
            wire_2, wires, instructions, cache
        )
    elif operation == "OR":
        result = evaluate(wire_1, wires, instructions, cache) | evaluate(
            wire_2, wires, instructions, cache
        )
    else:
        result = evaluate(wire_1, wires, instructions, cache) ^ evaluate(
            wire_2, wires, instructions, cache
        )

    cache[wire] = result

    return result


def to_decimal(circuit):
    return int(
        "".join(list(map(str, circuit.values()))),
        2,
    )


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
