# 15 Hardware and Virtual Machines 硬件与虚拟机

## 15.1 Processors, Parallel Processing and Virtual Machines 处理器，并行处理与虚拟机

### Complex Instruction Set Computer (CISC) 复杂指令集架构

a type of instruction set architecture. It contains more instructions that are
more complex and in more varying formats.  Arithmetic instructions can use data
in the memory as operands. Example: x86, x86-64.

### Reduced Instruction Set Computer (RISC) 精简指令集架构

a type of instruction set architecture. It contains fewer, simpler instructions
in a few formats. Only load and store instructions can access the memory.
Example: ARM, RISC-V.

### pipelining 流水线

instruction-level parallelism that allows several instructions to be processed
simultaneously, increasing the number of instructions completed per unit of time.

### parallel processing 并行处理

operation which allows a process to be split up and for each part to be executed
by a different processor at the same time.

### Single Instruction, Single Data (SISD) 单指令流单数据流

a basic computer architecture, which uses a single processor that can handle
a single instruction, and which also uses one data source at a time.

### Single Instruction, Multiple Data (SIMD) 单指令流多数据流

a basic computer architecture, in which a control unit (CU) controls an array
of many ALUs to execute the same instruction using different data inputs.
Many GPUs are SIMD.

### Multiple Instruction, Single Data (MISD) 多指令流单数据流

a basic computer architecture, in which many processors execute different
instructions using the same data set.

### Multiple Instruction, Multiple Data (MIMD) 多指令流多数据流

a basic computer architecture, in which many processors execute different
instructions using different data sets.

### massively parallel computers 大规模并行计算机

a large number of computer processors or separate computers, linked together
via network infrastructure and communicate using a message interface,
to simultaneously perform a set of coordinated computations.

### virtual machine 虚拟机

the **emulation** of a computer system on a host computer system. A virtual
machine implementation software (hypervisor) emulates the virtual hardware,
and a guest operating system(s) runs on the virtual machine manages it.

## 15.2 Boolean Algebra and Logic Circuits 布尔代数与逻辑电路

### Combinational circuit 组合逻辑电路

a logical circuit in which the output is dependent only on the input values.
Examples: almost all the logical circuits encounterd in A level Computer
Science, including half adder and full adder.

### Sequential circuit 时序逻辑电路

a logical circuit in which the output depends not only on the input values,
but also on the previous output via feedback.  Examples: flip-flop.

### Half adder circuit 半加器

a logical circuit that carries out binary addition on two bits, giving sum and
carry.

### Full adder circuit 全加器

two half adders combined to allow the sum of several binary bits.

### flip-flop 触发器

a logical circuit with two stable states that is used to stores a single bit.

