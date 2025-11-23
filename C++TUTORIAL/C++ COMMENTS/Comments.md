# C++ Comments

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)

## Overview

Comments can be used to explain C++ code, and to make it more readable. It can also be used to prevent execution when testing alternative code. Comments can be singled-lined or multi-lined.

Single-line Comments
Single-line comments start with two forward slashes (//).

Any text between // and the end of the line is ignored by the compiler (will not be executed).

This example uses a single-line comment before a line of code:

## Example 1

```cpp
// This is a comment
cout << "Hello World!";
```

This example uses a single-line comment at the end of a line of code:

## Example 2

```cpp
cout << "Hello World!"; // This is a comment
```

C++ Multi-line Comments
Multi-line comments start with /_ and ends with _/.

Any text between /_ and _/ will be ignored by the compiler:

## Example 3

/_ The code below will print the words Hello World!
to the screen, and it is amazing _/
cout << "Hello World!";
Single or multi-line comments?
It is up to you which you want to use. Normally, we use // for short comments, and /\* \*/ for longer.
