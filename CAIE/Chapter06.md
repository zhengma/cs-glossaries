### opcode 操作码
defines the action associated with the instruction.

### operand 操作数
defines any data needed by the instruction 

### machine code 机器码
the language that the CPU uses directly.

### instruction 指令
a single operation CPU performs.  Each instruction is represented by a binary
code with a defined number of bits that comprises an opcode and, most often,
one or more operand.

### instruction set 指令集
the complete set of machine code instructions use by a CPU.

### assembly language 汇编语言
a low-level language related to machine code where opcodes are written as
mnemonics and there is a character representation for an operand.

### source code 源码
a computer program that is not written in machine code and has to be translated
before execution.

### object code 目标码
the machine code program translated from a source code.

### assembler 汇编器
a program used to translate an assembly language program into machine code.

### directive 伪指令
an instruction to the assembler program.

### addressing mode 寻址模式
method of using the operand to find the value used by the instruction.

### direct addressing 直接寻址
an addressing mode in which the operand is the memory address of the value used.

### indirect addressing 间接寻址
an addressing mode in which the operand is the memory address of a “pointer”,
which in turn holds the memory address of the value used.

### index addressing 索引寻址
an addressing mode in which the memory address of the value used is
“operand + content in IX register”.

### immediate addressing 立即数寻址
an addressing mode in which the operand itself is the value used.

### logical shift 逻辑移位
where bits in the accumulator are shifted to the right or to the left and zero
moves into the bit position vacated

### cyclic shift 循环移位
similar to a logical shift but bits shifted from one end reappear at the other
end.

### arithmetic shift 算术移位
similar to a logical shift but the sign of the number is preserved.  Used in
multiplication or division of a signed integer stored in the accumulator.