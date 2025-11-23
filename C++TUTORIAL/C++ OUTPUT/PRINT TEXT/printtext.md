# C++ Output (Print Text)

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)

## Overview

The cout object, together with the << operator, is used to output values/print text:

## Example 1

```cpp
#include <iostream>
using namespace std;

int main() {
cout << "Hello World!";
return 0;
}
```

You can add as many cout objects as you want. However, note that it does not insert a new line at the end of the output:

## Example 2

```cpp
#include <iostream>
using namespace std;

int main() {
cout << "Hello World!";
cout << "I am learning C++";
return 0;
}
```
