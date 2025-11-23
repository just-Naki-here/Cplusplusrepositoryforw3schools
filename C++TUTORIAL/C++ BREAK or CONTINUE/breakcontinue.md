# C++ Break

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)

## Overview

You have already seen the break statement used in an earlier chapter of this tutorial. It was used to "jump out" of a switch statement.

The break statement can also be used to jump out of a loop.

This example jumps out of the loop when i is equal to 4:

## Example 1

```cpp
for (int i = 0; i < 10; i++) {
if (i == 4) {
break;
}
cout << i << "\n";
}
```

C++ Continue
The continue statement breaks one iteration (in the loop), if a specified condition occurs, and continues with the next iteration in the loop.

This example skips the value of 4:

## Example 2

```cpp
for (int i = 0; i < 10; i++) {
if (i == 4) {
continue;
}
cout << i << "\n";
}
```

Break and Continue in While Loop
You can also use break and continue in while loops:

Break Example
int i = 0;
while (i < 10) {
cout << i << "\n";
i++;
if (i == 4) {
break;
}
}
Continue Example
int i = 0;
while (i < 10) {
if (i == 4) {
i++;
continue;
}
cout << i << "\n";
i++;
}
