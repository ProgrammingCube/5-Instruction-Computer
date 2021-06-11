# Python 5 Instruction Computer
A python implementation of the [WDR paper computer](https://en.wikipedia.org/wiki/WDR_paper_computer)

## Introduction
This project is meant to help coders understand just _what_ assembly language is, and just _what_ the CPU is doing under the hood.

With only 5 instructions, this "CPU" implementation is certainly simple. But because it includes a branching jump, it is, in fact, [turing complete](https://en.wikipedia.org/wiki/Turing_completeness).

## Installation

In order to use this program, you must have Python 3.5 or later installed.

Next, you need to install [PyQt5](https://pypi.org/project/PyQt5/). This is the window manager, style sheet, and function handler for pretty much everything (I <ins>HIGHLY</ins> recommend using PyQt5 for your projects, its designer is a joy to use.)

To install pyqt5 via pip:

`$pip install pyqt5`

To install via your package manager:

`$sudo apt install python-pyqt5`

Now you can clone this repository and start programming!

## Instructions

1. [inc](#incdescriptor)
1. [dec](#decdescriptor)
1. [isz](#iszdescriptor)
1. [jmp](#jmpdescriptor)
1. [stp](#stpdescriptor)

## Theory

The idea of the WDR-1 computer is that is a very simple system to learn the theory of computing on. The idea of a Turing machine is the ability to conditionally branch code and, by extension, change data conditionally. With this ability, one is able to solve any algorithm in this universe...given enough time, space, and brainpower.


## Instructions
[R] - Register
[L] - Line number
### INC
Syntax: INC [R]

This instruction increments the target register by 1.

### DEC
Syntax: DEC [R]

This instruction decrements the target register by 1. Note that one is unable to have a negative in a register.

### ISZ
Syntax: ISZ [R]

This instruction checks to see if the target register is zero. If [R] is zero, then increment the program counter +2 lines. If not, then increment the program counter +1 line.

### JMP
Syntax: JMP [L]

This is an unconditional jump to line number [L].

### STP
Syntax: STP

This instruction halts the computer's execution.

## Examples

1. helloworld.txt
  - Toggles Register A from 0 to 1 and back, forever.
2. unsigned_2way_multiply.txt
  - A non-working example.
3. unsigned_multiply.txt
  - Multiplies contents of Register A by Register B and puts the result in Register C.
4. \boolean\*.txt
  - These examples do boolean functions on Register A and Register B.
5. simple arithmetic\signed_subtract.txt
  - Subtracts Register B from Register A. If negative, Register X is flagged.
6. simple arithmetic\simple_add.txt
  - Adds Register A to Register B.
7. simple arithmetic\simple_subract.txt
  - Subracts Register B from Register A.
