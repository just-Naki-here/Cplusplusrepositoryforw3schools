# Return Values

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)

## Overview

The void keyword, used in the previous examples, indicates that the function should not return a value. If you want the function to return a value, you can use a data type (such as int, string, etc.) instead of void, and use the return keyword inside the function:

## Example 1

```cpp
int myFunction(int x) {
return 5 + x;
}

int main() {
cout << myFunction(3);
return 0;
}

// Outputs 8 (5 + 3)
```

This example returns the sum of a function with two parameters:

## Example 2

```cpp
int myFunction(int x, int y) {
return x + y;
}

int main() {
cout << myFunction(5, 3);
return 0;
}

// Outputs 8 (5 + 3)
```

You can also store the result in a variable:

## Example 3

```cpp
int myFunction(int x, int y) {
return x + y;
}

int main() {
int z = myFunction(5, 3);
cout << z;
return 0;
}
// Outputs 8 (5 + 3)
```
