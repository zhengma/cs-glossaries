### von Neumann architecture 冯·诺伊曼架构
computer architecture with the following features: has a processor that directly
accesses to the memory; the memory stores both programs and data; program
consists of instructions that the processor executes sequentially.

### arithmetic and logic unit (ALU) 算术逻辑单元
component in the processor that carries out all arithmetic and logical
operations.

### control unit (CU) 控制单元
component in the processor that controls the data flow in the computer system
and ensures the instructions are handled correctly.

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
a special-purpose register, each bit of which (called a “flag”) can be
referenced independently and is set or cleared to mean special status.

### program counter (PC) 程序计数器
a special-purpose register that stores the memory address of the next
instruction.

### current instruction register (CIR) 当前指令寄存器
a special-purpose register that stores the current instruction while it’s being
decoded and executed.

### memory address register (MAR) 内存地址寄存器
a special-purpose register that stores the address (in the memory or in an I/O
device) about to be accessed.

### memory data register (MDR) 内存数据寄存器
a special-purpose register that the data just read from (or about to be written
to) the memory.

### index register (IX) 索引寄存器
a register used for index addressing.

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
signal sent from a device or software to a processor, requesting it to suspends
the current operations and serve the interrupt first.  Causes include fatal
error in program or in hardware, need of I/O.

### interrupt service routine (ISR) 中断处理程序
a program which handles specific type of interrupt requests.
