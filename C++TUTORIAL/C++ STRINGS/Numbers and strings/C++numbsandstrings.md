# Adding Numbers and Strings

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)

## Overview

\\WARNING!
\\
\\C++ uses the + operator for both addition and concatenation.
\\
\\Numbers are added. Strings are concatenated.

If you add two numbers, the result will be a number:

## Example 1

```cpp
int x = 10;
int y = 20;
int z = x + y; // z will be 30 (an integer)
```

If you add two strings, the result will be a string concatenation:

## Example 2

```cpp
string x = "10";
string y = "20";
```

string z = x + y; // z will be 1020 (a string)
If you try to add a number to a string, an error occurs:

## Example 3

```cpp
string x = "10";
int y = 20;
string z = x + y;
```
