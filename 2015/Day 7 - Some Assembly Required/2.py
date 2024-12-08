import re


def main():
    lines = read_puzzle()
    
    wires = run_circuit(lines)
    lines = replace_b(lines, wires["a"])
    wires = run_circuit(lines)
    
    print(wires["a"])


def run_circuit(instructions_list):
    instructions = {}

    for instruction in instructions_list:
        parsed = parse_instruction(instruction)
        wire = parsed[3]
        instructions[wire] = parsed

    results = {wire: evaluate(wire, instructions, {}) for wire in instructions}

    return results


def parse_instruction(instruction):
    if "AND" in instruction:
        m = re.match(r"(\w+) AND (\w+) -> (\w+)", instruction)
        return ("AND", m.group(1), m.group(2), m.group(3))
    elif "OR" in instruction:
        m = re.match(r"(\w+) OR (\w+) -> (\w+)", instruction)
        return ("OR", m.group(1), m.group(2), m.group(3))
    elif "LSHIFT" in instruction:
        m = re.match(r"(\w+) LSHIFT (\d+) -> (\w+)", instruction)
        return ("LSHIFT", m.group(1), int(m.group(2)), m.group(3))
    elif "RSHIFT" in instruction:
        m = re.match(r"(\w+) RSHIFT (\d+) -> (\w+)", instruction)
        return ("RSHIFT", m.group(1), int(m.group(2)), m.group(3))
    elif "NOT" in instruction:
        m = re.match(r"NOT (\w+) -> (\w+)", instruction)
        return ("NOT", m.group(1), None, m.group(2))
    else:
        m = re.match(r"(\w+|\d+) -> (\w+)", instruction)
        return ("ASSIGN", m.group(1), None, m.group(2))


def evaluate(wire, instructions, cache):
    if wire.isdigit():
        return int(wire)

    if wire in cache:
        return cache[wire]

    operation, wire_1, wire_2, _ = instructions[wire]

    if operation == "ASSIGN":
        result = evaluate(wire_1, instructions, cache)
    elif operation == "AND":
        result = evaluate(wire_1, instructions, cache) & evaluate(
            wire_2, instructions, cache
        )
    elif operation == "OR":
        result = evaluate(wire_1, instructions, cache) | evaluate(
            wire_2, instructions, cache
        )
    elif operation == "LSHIFT":
        result = evaluate(wire_1, instructions, cache) << wire_2
    elif operation == "RSHIFT":
        result = evaluate(wire_1, instructions, cache) >> wire_2
    elif operation == "NOT":
        result = ~evaluate(wire_1, instructions, cache) & 0xFFFF

    cache[wire] = result

    return result

def replace_b(lines, wire_a):
    return [f"{wire_a} -> b" if "b" in line else line for line in lines]


def read_puzzle():
    f = open("puzzle.txt", "r")
    lines = f.read().splitlines()
    f.close()

    return lines


if __name__ == "__main__":
    main()
