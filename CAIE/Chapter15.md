# 15 Hardware and VM 硬件与虚拟机

## 15.1 Processors, Parallel Processing and Virtual Machines 处理器，并行处理与虚拟机

### Complex Instruction Set Computer (CISC) 复杂指令集架构

a type of instruction set architecture. It contains more instructions that are
more complex and are more varying in lengths and formats, some taking several
clock cycles. It has fewer registers but more addressing modes, and have
programmable control unit.
Example: x86, x86-64.

### Reduced Instruction Set Computer (RISC) 精简指令集架构

a type of instruction set architecture. It contains fewer, simpler instructions
that have fixed lengths and are in only a few formats, most of which take only
one clock cycle. It has many registers, but most instructions cannot access
memory directly.
Example: ARM, RISC-V.

### pipelining 流水线

instruction-level parallelism that allows several instructions to be processed
simultaneously, increasing the number of instructions completed per unit of time.

### parallel processing 并行处理

operation which allows a process to be split up and for each part to be executed
by a different processor at the same time.

### Single Instruction, Single Data (SISD) 单指令流单数据流

a basic computer architecture, which uses a single processor that can handle
a single instruction at a time, using data from a single source. It contains one
processor, a control unit and a memory unit that executes instructions sequentially.

### Single Instruction, Multiple Data (SIMD) 单指令流多数据流

a basic computer architecture, in which a control unit (CU) controls an array
of many ALUs to execute the same instruction using different data inputs
simultaneously. The instructions can be performed sequentially, taking advantage
of pipelining. It can also be parallel computers **with** multiple processors.
Many GPUs are SIMD.

### Multiple Instruction, Single Data (MISD) 多指令流单数据流

a basic computer architecture, in which many processors execute different
instructions using the same data stream. Each processor works on the same data
stream independently.  It can also be parallel computers **with** multiple
processors.

### Multiple Instruction, Multiple Data (MIMD) 多指令流多数据流

a basic computer architecture, in which many processors that operate independently,
execute different instructions using different data sets.

### massively parallel computers 大规模并行计算机

a large number of computer processors or separate computers, linked together
via network infrastructure and communicate using a message interface,
to simultaneously perform a set of coordinated computations.

### virtual machine (VM) 虚拟机

the **emulation** of a computer system on a host computer system. A virtual
machine implementation software (hypervisor) emulates the virtual hardware,
and a guest operating system(s) runs on the virtual machine manages it.

### host machine 物理计算机

also known as *host computer*. A physical computer running the host operating
system, on which a hypervisor run as an application software.

### hypervisor 虚拟机管控程序

also known as virtual machine software or. An application software that runs on
the host machine. It emulates the virtual machine and provides a platform on
which the guest system runs.

### host operating system 宿主操作系统

the normal operating system for the host machine that controls the resources of it.
It runs the hypervisor and provides a user interface to operate it.

### guest operating system 客操作系统

the operating system runs within the virtual machine that controls the virtual
hardware/software during the emulation and accesses the physical (actual)
hardware through the virtual machine and the host operating system.
It runs under the control of the host operating system, providing a virtual
user interface for the emulated hardware/software.

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
