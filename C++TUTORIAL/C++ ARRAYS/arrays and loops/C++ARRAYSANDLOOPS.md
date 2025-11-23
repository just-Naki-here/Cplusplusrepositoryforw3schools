# Loop Through an Array

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)
- [Example 4](#example-4)
- [Example 5](#example-5)

## Overview

You can loop through the array elements with the for loop.

The following example outputs all elements in the cars array:

## Example 1

```cpp
// Create an array of strings
string cars[5] = {"Volvo", "BMW", "Ford", "Mazda", "Tesla"};

// Loop through strings
for (int i = 0; i < 5; i++) {
cout << cars[i] << "\n";
}
```

This example outputs the index of each element together with its value:

## Example 2

```cpp
string cars[5] = {"Volvo", "BMW", "Ford", "Mazda", "Tesla"};
for (int i = 0; i < 5; i++) {
cout << i << " = " << cars[i] << "\n";
}
```

And this example shows how to loop through an array of integers:

## Example 3

```cpp
int myNumbers[5] = {10, 20, 30, 40, 50};
for (int i = 0; i < 5; i++) {
cout << myNumbers[i] << "\n";
}
```

The foreach Loop
There is also a "for-each loop" (introduced in C++ version 11 (2011)), which is used exclusively to loop through elements in an array (and other data structures, like vectors and lists):

Syntax
for (type variableName : arrayName) {
// code block to be executed
}
The following examples output all elements in an array using a "for-each loop":

## Example 4

Loop through integers:

// Create an array of integers
int myNumbers[5] = {10, 20, 30, 40, 50};

// Loop through integers
for (int i : myNumbers) {
cout << i << "\n";
}
## Example 5

Loop through strings:

// Create an array of strings
string cars[5] = {"Volvo", "BMW", "Ford", "Mazda", "Tesla"};

// Loop through strings
for (string car : cars) {
cout << car << "\n";
}
