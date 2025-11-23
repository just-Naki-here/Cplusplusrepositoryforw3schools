# Get Memory Address and Value

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)

## Overview

In the example from the previous page, we used the pointer variable to get the memory address of a variable (used together with the & reference operator). However, you can also use the pointer to get the value of the variable, by using the \* operator (the dereference operator):

## Example 1

string food = "Pizza"; // Variable declaration
string\* ptr = &food; // Pointer declaration

// Reference: Output the memory address of food with the pointer (0x6dfed4)
cout << ptr << "\n";

// Dereference: Output the value of food with the pointer (Pizza)
cout << _ptr << "\n";
Note that the _ sign can be confusing here, as it does two different things in our code:

When used in declaration (string\* ptr), it creates a pointer variable.
When not used in declaration, it act as a dereference operator.
