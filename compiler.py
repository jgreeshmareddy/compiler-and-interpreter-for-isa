import json
import sys

# Load ISA spec
isa = json.load(open("isa.json", "r"))
instr_set = isa["INSTRUCTIONS"]

def error(msg):
    print(f"[COMPILER ERROR] {msg}")
    sys.exit(1)

def parse_line(line, line_no):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    
    tokens = line.replace(",", "").split()
    mnemonic = tokens[0].upper()

    if mnemonic not in instr_set:
        error(f"Line {line_no}: Unknown instruction '{mnemonic}'")

    fmt = instr_set[mnemonic]["format"].split(",")

    if fmt == [""]:
        if len(tokens) != 1:
            error(f"Line {line_no}: '{mnemonic}' takes no arguments")
        return (mnemonic, [])

    if len(tokens) - 1 != len(fmt):
        error(f"Line {line_no}: Expected {len(fmt)} arguments, got {len(tokens)-1}")
    
    return (mnemonic, tokens[1:])

def encode(instr, args):
    opcode_map = {
        "LOAD": "00",
        "STORE_W": "01",
        "STORE_B": "02",
        "MAC": "03",
        "ADD": "04",
        "SUB": "05",
        "HALT": "FF"
    }

    opcode = opcode_map[instr]

    if instr == "HALT":
        return opcode

    enc = opcode
    for a in args:
        enc += f" {a}"

    return enc

def compile_file(inp, out):
    machine_code = []
    with open(inp, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        parsed = parse_line(line, i)
        if parsed:
            instr, args = parsed
            machine_code.append(encode(instr, args))
    
    open(out, "w").write("\n".join(machine_code))
    print("[COMPILER] Done. Output ->", out)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compiler.py input.txt output.txt")
        sys.exit(1)

    compile_file(sys.argv[1], sys.argv[2])

