# interpreter.py  executes NN-ISA
import sys

R = [0]*8
W = [0]*8
B = [0]*8

def relu(x):
    return x if x > 0 else 0

def run_instruction(inst):
    global R, W, B

    op = int(inst[0:4], 2)
    d  = int(inst[4:8], 2)
    s1 = int(inst[8:12], 2)
    s2 = int(inst[12:16], 2)

    if op == 0x1:  # LOAD_IMM
        R[d] = s1*16 + s2

    elif op == 0x2:  # LOAD_W
        R[d] = W[s1]

    elif op == 0x3:  # LOAD_B
        R[d] = B[s1]

    elif op == 0x4:  # STORE_W
        W[d] = R[s1]

    elif op == 0x5:  # STORE_B
        B[d] = R[s1]

    elif op == 0x6:  # MAC
        R[d] = R[s1] * R[s2]

    elif op == 0x7:  # ADD
        R[d] = R[s1] + R[s2]

    elif op == 0x8:  # SUB
        R[d] = R[s1] - R[s2]

    elif op == 0x9:  # RELU
        R[d] = relu(R[s1])

    elif op == 0xA:  # UPDATE_W
        W[d] = R[s1]

    elif op == 0xB:  # UPDATE_B
        B[d] = R[s1]

    elif op == 0xF:  # HALT
        return False

    return True

def run_program(machine_code):
    for inst in machine_code:
        if not run_instruction(inst):
            break

if __name__ == "__main__":
    program = sys.stdin.read().strip().split()
    run_program(program)
    print("Registers:", R)
    print("Weights:", W)
    print("Biases:", B)
