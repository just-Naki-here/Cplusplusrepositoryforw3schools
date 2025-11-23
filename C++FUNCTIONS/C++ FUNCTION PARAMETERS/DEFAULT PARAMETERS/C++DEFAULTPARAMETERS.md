# Default Parameter Value

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)

## Overview

You can also use a default parameter value, by using the equals sign (=).

If we call the function without an argument, it uses the default value ("Norway"):

## Example 1

```cpp
void myFunction(string country = "Norway") {
cout << country << "\n";
}

int main() {
myFunction("Sweden");
myFunction("India");
myFunction();
myFunction("USA");
return 0;
}

// Sweden
// India
// Norway
// USA
```

A parameter with a default value, is often known as an "optional parameter". From the example above, country is an optional parameter and "Norway" is the default value.
