# C++ Loops

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)

## Overview

Loops can execute a block of code as long as a specified condition is reached.

Loops are handy because they save time, reduce errors, and they make code more readable.

C++ While Loop
The while loop loops through a block of code as long as a specified condition is true:

Syntax
while (condition) {
// code block to be executed
}
In the example below, the code in the loop will run, over and over again, as long as a variable (i) is less than 5:

## Example 1

```cpp
int i = 0;
while (i < 5) {
cout << i << "\n";
i++;
}
```

Note: Do not forget to increase the variable used in the condition, otherwise the loop will never end!
