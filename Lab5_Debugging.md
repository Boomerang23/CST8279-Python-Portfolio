# Lab 5 – Debugging a Python Function

## Project Overview

This project was completed for CST8279 – Introduction to Computer Programming Using Python.

The objective was to debug a Python function that was supposed to find the minimum value in a list without using Python's built-in 'min()' function.

## Problem Identified

The original program initialized the minimum value to '0'. This caused incorrect results when all values in the list were positive.

For example, with the list:

'[5, 12, 3, 8]'

the program returned '0' instead of the correct minimum value, '3'.

## Solution

I used debugging techniques to monitor the value of the variable during each iteration.

The solution was to initialize the minimum value using the first element of the list and then compare the remaining elements against it.

## Skills Demonstrated

- Python debugging
- Problem-solving
- Lists
- Loops
- Conditional statements
- Functions
- Testing and code correction

## Project File

- 'Lab5_Ange.Gbocho.docx'  Debugging analysis, corrected solution, testing, and references
