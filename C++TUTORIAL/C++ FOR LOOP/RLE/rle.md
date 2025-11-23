# Real Life Example

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)
- [Example 4](#example-4)
- [Example 5](#example-5)

## Overview

To demonstrate a practical example of the for loop, let's create a program that counts to 100 by tens:

## Example 1

```cpp
for (int i = 0; i <= 100; i += 10) {
cout << i << "\n";
}
```

In this example, we create a program that only print even numbers between 0 and 10 (inclusive):

## Example 2

```cpp
for (int i = 0; i <= 10; i = i + 2) {
cout << i << "\n";
}
```

Here we only print odd numbers:

## Example 3

```cpp
for (int i = 1; i <= 10; i = i + 2) {
cout << i << "\n";
}
```

In this example we print the powers of 2 up to 512:

## Example 4

```cpp
for (int i = 2; i <= 512; i \*= 2) {
cout << i << "\n";
}
```

And in this example, we create a program that prints the multiplication table for a specified number:

## Example 5

```cpp
int number = 2;
int i;

// Print the multiplication table for the number 2
for (i = 1; i <= 10; i++) {
cout << number << " x " << i << " = " << number \* i << "\n";
}
```
