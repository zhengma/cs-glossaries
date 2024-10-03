# 5 System Software 系统软件

## 5.1 Operating System 操作系统

### operating system (OS) 操作系统

a software platform that provides facilities for programs to be run and
provides interface between hardware and software.

### the Four Basic Tasks of Operating System 操作系统的四大基本任务

process management, memory management, hardware management and file management.
Sometimes a fifth task is included: security management.

### process 进程

a program that has begun execution.

### process management 进程管理

part of the OS that allocates resources (mainly CPU time and memory) to
different processes and permits sharing and exchange of data.

### memory management 内存管理

part of the OS that controls the main memory.  Tasks including memory
optimisation, memory organisation and memory protection.

### hardware management 硬件管理

part of the OS that controls all I/O devices connected to the computer and
their usage by the processes. The OS installs device drivers to allow
communication between the devices and the computer, handles the buffer for
such transmission, and manage interrupts.

### file 文件

a collection of data stored by a computer program to be used again.

### file management 文件管理

part of the OS in charge of the provision of file name conventions, directory
structures and access control of files.

### security management 安全管理

part of the OS that ensures the integrity, confidentiality and availability
of data.

### utility software 实用软件

program that is not executed as part of the normal running of the OS but is
run when needed.  It can be provided along with the OS or be installed
separately.

### disk formatter 磁盘格式化工具

utility software that initialises a disk, allowing files to be stored in and
retrieved from it.

### disk checker 磁盘检查工具

utility software that checks disk drives for errors and inconsistencies, and
repair errors if possible.

### disk defragmenter 磁盘碎片整理工具

utility software that reorganises the sectors on an HDD, so that individdual
files are stored on contiguous sectors, improving disk access times.

### backup software 备份软件

utility software that makes copies of files **at regular intervals** on a
portable storage device, so that lost data can be **retrieved**. 

### antivirus software 杀毒软件

utility software that quarantines and deletes files infected by virus.

### program Library 程序库

a collection of pre-written programs and modules stored on a computer that
software developers can import or call in their own programs.

### static linking 静态链接

the object code of a library program or module is linked to the program calling
it when compiling the latter, and is incorporated into the executable code file.

### dynamic linking 动态链接

the object code of a library program or module is stored in a separate file
(DLL) and is linked to the program calling it only at the running time.

## 5.2 Language Translator 语言处理程序

### translator

a system software that translate a source code written in any language other
than machine code into machine code.  Including assembler, compiler and interpreter.

### compiler 编译器

a translator that translate the whole source code in high-level language into
object code and, if successful, store it on the disk as an executable file.

### interpreter 解释器

a translator that analyses and executes a program in high-level language line
by line, stopping when an error is encountered.

### debugging 调试

finding and correcting errors often called ‘bugs’, in a program.

### integrated Development Environment (IDE) 集成开发环境

a suite of programs used to write and test the source code in a high-level
programming language. Main features include: context-sensitive prompts,
auto-correct, syntax highlighting, expand/collapse code blocks,
single-stepping and setting breakpoints.

### context-sensitive prompts 自动补全

give suggestions for code as the user types.

### auto-correct 自动修正

correct the spelling mistakes in the code.

### pretty-printing (syntax highlighting) 漂亮输出 (语法高亮)

use different colours to display different tokens in the source code, making
it easier to read.

### collapse code blocks 代码块折叠

hide the code not currently being worked on.

### single-stepping 单步执行

run the code one line at a time and watch the effect of each line.

### breakpoint 断点

stop the code running at a set point to check the variable contents.
