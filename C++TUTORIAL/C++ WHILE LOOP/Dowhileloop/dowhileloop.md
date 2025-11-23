# The Do/While Loop

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)

## Overview

The do/while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.

Syntax
do {
// code block to be executed
}
while (condition);
The example below uses a do/while loop. The loop will always be executed at least once, even if the condition is false, because the code block is executed before the condition is tested:

## Example 1

```cpp
int i = 0;
do {
cout << i << "\n";
i++;
}
while (i < 5);
```

Do not forget to increase the variable used in the condition, otherwise the loop will never end!
