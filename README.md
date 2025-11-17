🧩 Project Components

The project contains three main components:

ISA Specification (isa.md)
Compiler (compiler.py)
Interpreter (interpreter.py)

Together, these simulate the NN accelerator before the real hardware chip is available.

⚙️ 1. ISA Specification

The ISA defines the instructions supported by the neural-network accelerator.
Each instruction is 16 bits:

          -------------------------------------------------
          | OPCODE (4) | DEST (4) | SRC1 (4) | SRC2 (4) |
          -------------------------------------------------

🧮 Registers

            R0–R7: General-purpose registers
            W0–W7: Weight memory addresses
            B0–B7: Bias memory addresses

📜 Instruction List

            Opcode	   Mnemonic   	Description
            0001     	LOAD_IMM	    Load immediate into register
            0010	    LOAD_W	      Load from weight memory
            0011	    LOAD_B	      Load from bias memory
            0100	    STORE_W	      Store register into weight memory
            0101	    STORE_B	      Store register into bias memory
            0110	    MAC	          Multiply–Accumulate (R[dest] = R[src1] * R[src2])
            0111	    ADD	          Addition
            1000	    SUB	          Subtraction
            1001	    RELU	        Rectified Linear Unit
            1010	    UPDATE_W	    Write updated weight
            1011	    UPDATE_B	    Write updated bias
            1111	    HALT	        Stop execution

This ISA is designed to match  Verilog hardware blocks for:

MAC computation  , ReLU , Weight & bias memories , Dynamic weight/bias update modules


🛠️ 2. Compiler (compiler.py)

The compiler converts assembly instructions like:
        
        LOAD_IMM R1, 5
        LOAD_IMM R2, 3
        MAC R3, R1, R2
        UPDATE_W W1, R3
        HALT


into machine code such as:

        0001000100000101
        0001001000000011
        0110001100010010
        1010000100110000
        1111000000000000

Key Functions:

        Converts mnemonics → opcodes
        Converts register names → 4-bit IDs
        Constructs the 16-bit instruction format
        Outputs binary machine code usable by the interpreter or hardware
        This machine code will eventually run on the physical chip.

🖥️ 3. Interpreter (interpreter.py)

Until the chip is available, the interpreter simulates its behavior.
It reads machine code and updates:

        Register file
        Weight memory
        Bias memory
        Performs MAC
        Applies RELU
        Supports weight/bias updates


🔄 Workflow (How the system works)
Step 1 — Write Assembly Program

        Example: program.asm
        
        LOAD_IMM R1, 10
        LOAD_IMM R2, 4
        MAC R3, R1, R2
        RELU R4, R3
        HALT

Step 2 — Compile to Machine Code

      Run:
      
          python compiler.py < program.asm > program.bin

Step 3 — Execute on Interpreter

      Run:
      
          python interpreter.py < program.bin


Output after interpretation:

      Registers: [0,5,3,15,0,0,0,0]
      Weights:   [15,0,0,0,0,0,0,0]
      Biases:    [0,0,0,0,0,0,0,0]
