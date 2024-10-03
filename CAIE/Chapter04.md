# 4 Processor Fundamentals 处理器基础

## 4.1 CPU Architecture 中央处理器架构

### von Neumann architecture 冯·诺伊曼架构

computer architecture with the following features: has a processor that directly
accesses to the memory; the memory stores both programs and data (stored program
concept); program consists of instructions that the processor executes
sequentially.

### arithmetic and logic unit (ALU) 算术逻辑单元

component in the processor that carries out all arithmetic and logical
operations.

### control unit (CU) 控制单元

component in the processor that coordinates the actions of other components,
controls the data flow in the computer system and ensures the instructions are
handled correctly.

### system clock 系统时钟

produces timing signal on the control bus to synchronise activities in a
computer.  Strictly speaking there are two clocks, one (internal clock)
synchronise activities inside the processor, and the other (system clock)
synchronise activities between the inside and the outside.

### register 寄存器

storage components in the processor that temporarily hold data or instructions
and have very short access time.  Can be general purpose or special purpose.

### accumulator 累加器

a general-purpose register that stores a numerical value before and after the
execution of an instruction by the ALU.

### status register (SR) 状态寄存器

a special-purpose register, each bit of which (called a "flag") can be
referenced independently and is set by events.

### program counter (PC) 程序计数器

a special-purpose register that stores the memory address of the **next**
instruction.

### current instruction register (CIR) 当前指令寄存器

a special-purpose register that stores the current instruction while it’s being
decoded and executed.

### memory address register (MAR) 内存地址寄存器

a special-purpose register that stores the address (in the memory or in an I/O
device) about to be accessed.

### memory data register (MDR) 内存数据寄存器

a special-purpose register that stores the data just read from (or about to be written
to) the memory.

### index register (IX) 索引寄存器

a special-purpose register that stores a value that is added to an address to
give another address.

### address bus 地址总线

a component that carries an address to the memory controller to access the
memory location or to the I/O system to identify the source or destination of
the data.

### data bus 数据总线

a component that carries data from the processor to the memory or to an output
device or can carry data from the memory or from an input device.

### control bus 控制总线

a component that carries signal from the CU to all other computer components.

### word 字

a group of bits that can be handled as a single unit by the computer system.

### Basic Input/Output System (BIOS) 基本输入/输出系统

a bootstrap program that is the first to run when a computer is turned on.
It’s usually stored on a ROM chip.

### port 端口

external connection to a computer which allows it to communicate with various
peripheral devices.

### Universal Serial Bus (USB) 通用串行总线

standard port connecting device to a computer that allows plug-and-play.

### High-definition Multimedia Interface (HDMI) 高清晰度多媒体接口

type of port connecting devices (usually video output devices such as screen,
monitor or projector) to a computer.  It transmits both video and audio signals.

### Video Graphics Array (VGA) 视频图形阵列

type of port that has similar functionality as HDMI but only transmits video
signal.

### interrupt 中断

**signal sent** from a device or software to a processor, requesting it to suspends
the current operations and serve the interrupt first.  Causes include: fatal
error in program (e.g. division by zero) or in hardware, need of I/O.

### interrupt service routine (ISR) 中断处理程序

a program which handles specific type of interrupt requests.

## 4.2 Assembly Language 汇编语言

### opcode 操作码

defines the action associated with the instruction.

### operand 操作数

defines any data needed by the instruction.

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

## 4.3 Bit Manipulation 位操纵

### logical shift 逻辑移位

where bits in the accumulator are shifted to the right or to the left and zero
moves into the bit position vacated

### cyclic shift 循环移位

similar to a logical shift but bits shifted from one end reappear at the other
end.

### arithmetic shift 算术移位

similar to a logical shift but the sign of the number is preserved.  Used in
multiplication or division of a signed integer stored in the accumulator.
