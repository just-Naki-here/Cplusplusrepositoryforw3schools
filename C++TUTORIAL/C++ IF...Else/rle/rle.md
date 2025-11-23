# Real Life Example

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)
- [Example 4](#example-4)

## Overview

This example shows how you can use if..else to "open a door" if the user enters the correct code:

## Example 1

```cpp
int doorCode = 1337;

if (doorCode == 1337) {
cout << "Correct code.\nThe door is now open.\n";
```

} else {
cout << "Wrong code.\nThe door remains closed.\n";
}
This example shows how you can use if..else to find out if a number is positive or negative:

## Example 2

```cpp
int myNum = 10; // Is this a positive or negative number?

if (myNum > 0) {
cout << "The value is a positive number.\n";
```

} else if (myNum < 0) {
cout << "The value is a negative number.\n";
} else {
cout << "The value is 0.\n";
}
Find out if a person is old enough to vote:

## Example 3

```cpp
int myNum = 10; // Is this a positive or negative number?

if (myNum > 0) {
cout << "The value is a positive number.\n";
```

} else if (myNum < 0) {
cout << "The value is a negative number.\n";
} else {
cout << "The value is 0.\n";
}
Find out if a number is even or odd:

## Example 4

```cpp
int myNum = 5;

if (myNum % 2 == 0) {
cout << myNum << " is even.\n";
```

} else {
cout << myNum << " is odd.\n";
}
