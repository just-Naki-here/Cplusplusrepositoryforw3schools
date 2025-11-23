# Multilevel Inheritance

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)

## Overview

A class can also be derived from one class, which is already derived from another class.

In the following example, MyGrandChild is derived from class MyChild (which is derived from MyClass).

## Example 1

```cpp
// Base class (parent)
class MyClass {
public:
void myFunction() {
cout << "Some content in parent class." ;
}
};

// Derived class (child)
class MyChild: public MyClass {
};

// Derived class (grandchild)
class MyGrandChild: public MyChild {
};

int main() {
MyGrandChild myObj;
myObj.myFunction();
return 0;
}
```
