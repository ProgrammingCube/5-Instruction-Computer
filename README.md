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
1. [dec](#incdescriptor)
1. [isz](#incdescriptor)
1. [jmp](#incdescriptor)
1. [stp](#incdescriptor)

## Theory

The first thing you need to 