# There is also a short-hand if else, which is known as the ternary operator because it consists of three operands.

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)

## Overview

It can be used to replace multiple lines of code with a single line, and is often used to replace simple if else statements:

Syntax
variable = (condition) ? expressionTrue : expressionFalse;
Instead of writing:

## Example 1

```cpp
int time = 20;
if (time < 18) {
cout << "Good day.";
```

} else {
cout << "Good evening.";
}
You can simply write:

## Example 2

```cpp
int time = 20;
string result = (time < 18) ? "Good day." : "Good evening.";
cout << result;
```
