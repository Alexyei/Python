def decode(instruction, registers):
    elements = instruction.split()
    result = elements[:2]
    for i in range(2, len(elements)):
        if elements[i].isalpha():
            result.append(int(registers[elements[i]]))
        else:
            result.append(int(elements[i]))
    return tuple(result)


def mov(arguments, registers):
    registers[arguments[0]] = arguments[1]
    return 1


def inc(arguments, registers):
    registers[arguments[0]] = registers.get(arguments[0], 0) + 1
    return 1


def dec(arguments, registers):
    registers[arguments[0]] = registers.get(arguments[0], 0) - 1
    return 1


def jnz(arguments, registers):
    return arguments[1] if registers.get(arguments[0], 0) else 1


def execute(instruction, registers):
    # commands = {
    #     'mov': mov,
    #     'inc': inc,
    #     'dec': dec,
    #     'jnz': jnz
    # }
    command = decode(instruction, registers)
    #return commands[command[0]](command[1:], registers)
    if command[0]=='mov':
        registers[command[1]] = command[2]
        return 1
    elif command[0]=='inc':
        registers[command[1]] = registers.get(command[1], 0) + 1
        return 1
    elif command[0] == 'dec':
        registers[command[1]] = registers.get(command[1], 0) - 1
        return 1
    else:
        return command[2] if registers.get(command[1], 0) else 1


def simple_assembler(instructions):
    current_command = 0
    registers = {}
    while (current_command != len(instructions)):
        current_command += execute(instructions[current_command], registers)
    return registers


def main():
    print(simple_assembler(['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']))


if __name__ == "__main__":
    main()
