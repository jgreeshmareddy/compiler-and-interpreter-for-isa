# Simple NN-ISA (Instruction Set Architecture)

This ISA is designed to control the neural-network hardware blocks created in Verilog.
Each instruction is 16 bits.

-------------------------------------------------
| OPCODE (4) |  DEST (4) | SRC1 (4) | SRC2 (4) |
-------------------------------------------------

## Register File
R0 – R7 : General-purpose registers  
W0 – W7 : Weight memory addresses  
B0 – B7 : Bias memory addresses  

## Instruction List

0001 – LOAD_IMM   : R[DEST] ← immediate (SRC1,SRC2 combined)
0010 – LOAD_W     : R[DEST] ← W[SRC1]
0011 – LOAD_B     : R[DEST] ← B[SRC1]
0100 – STORE_W    : W[DEST] ← R[SRC1]
0101 – STORE_B    : B[DEST] ← R[SRC1]
0110 – MAC        : R[DEST] ← R[SRC1] * R[SRC2]
0111 – ADD        : R[DEST] ← R[SRC1] + R[SRC2]
1000 – SUB        : R[DEST] ← R[SRC1] - R[SRC2]
1001 – RELU       : R[DEST] ← relu(R[SRC1])
1010 – UPDATE_W   : W[DEST] ← R[SRC1]
1011 – UPDATE_B   : B[DEST] ← R[SRC1]
1111 – HALT
