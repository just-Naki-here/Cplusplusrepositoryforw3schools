# Strings - Special Characters

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)

## Overview

Because strings must be written within quotes, C++ will misunderstand this string, and generate an error:

string txt = "We are the so-called "Vikings" from the north.";
The solution to avoid this problem, is to use the backslash escape character.

The backslash (\) escape character turns special characters into string characters:

Escape character Result Description
\' ' Single quote
\" " Double quote
\\ \ Backslash

The sequence \" inserts a double quote in a string:

## Example 1

```cpp
string txt = "We are the so-called \"Vikings\" from the north.";
```


The sequence \' inserts a single quote in a string:

## Example 2

```cpp
string txt = "It\'s alright.";
```


The sequence \\ inserts a single backslash in a string:

## Example 3

```cpp
string txt = "The character \\ is called backslash.";
```


Other popular escape characters in C++ are:

Escape Character Result
\n New Line
\t Tab
