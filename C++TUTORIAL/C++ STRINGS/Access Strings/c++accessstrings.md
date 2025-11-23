# Access Strings

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)
- [Example 4](#example-4)
- [Example 5](#example-5)

## Overview

You can access the characters in a string by referring to its index number inside square brackets [].

This example prints the first character in myString:

## Example 1

```cpp
string myString = "Hello";
cout << myString[0];
// Outputs H
```

Note: String indexes start with 0: [0] is the first character. [1] is the second character, etc.
This example prints the second character in myString:

## Example 2

```cpp
string myString = "Hello";
cout << myString[1];
// Outputs e
```

To print the last character of a string, you can use the following code:

## Example 3

```cpp
string myString = "Hello";
cout << myString[myString.length() - 1];
// Outputs o
```

Change String Characters
To change the value of a specific character in a string, refer to the index number, and use single quotes:

## Example 4

```cpp
string myString = "Hello";
myString[0] = 'J';
cout << myString;
// Outputs Jello instead of Hello
```

The at() function
The <string> library also has an at() function that can be used to access characters in a string:

## Example 5

```cpp
string myString = "Hello";
cout << myString; // Outputs Hello

cout << myString.at(0); // First character
cout << myString.at(1); // Second character
cout << myString.at(myString.length() - 1); // Last character

myString.at(0) = 'J';
cout << myString; // Outputs Jello
```


Tip: A list of other useful string functions, can be found in the c++ reference folder
