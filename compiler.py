import sys

opcodes = {
    "LOAD_IMM": "0001",
    "LOAD_W"  : "0010",
    "LOAD_B"  : "0011",
    "STORE_W" : "0100",
    "STORE_B" : "0101",
    "MAC"     : "0110",
    "ADD"     : "0111",
    "SUB"     : "1000",
    "RELU"    : "1001",
    "UPDATE_W": "1010",
    "UPDATE_B": "1011",
    "HALT"    : "1111"
}

def reg_to_bin(r):
    return format(int(r[1:]), '04b')

def compile_line(line):
    parts = line.replace(",", "").split()
    op = parts[0]

    if op == "HALT":
        return opcodes["HALT"] + "00000000"

    dest = reg_to_bin(parts[1])
    src1 = reg_to_bin(parts[2]) if len(parts) > 2 else "0000"
    src2 = reg_to_bin(parts[3]) if len(parts) > 3 else "0000"

    return opcodes[op] + dest + src1 + src2

def compile_program(text):
    lines = text.strip().split("\n")
    machine = []
    for l in lines:
        if l.strip() == "" or l.strip().startswith("#"):
            continue
        machine.append(compile_line(l))
    return machine

if __name__ == "__main__":
    program = sys.stdin.read()
    out = compile_program(program)
    for x in out:
        print(x)
