C++ Booleans
Very often, in programming, you will need a data type that can only have one of two values, like:

YES / NO
ON / OFF
TRUE / FALSE
For this, C++ has a bool data type, which can take the values true (1) or false (0).

Boolean Values
A boolean variable is declared with the bool keyword and can take the values true or false:

Example
bool isCodingFun = true;
bool isFishTasty = false;
cout << isCodingFun;  // Outputs 1 (true)
cout << isFishTasty;  // Outputs 0 (false)
From the example above, you can read that a true value returns 1, and false returns 0.

However, it is more common to return a boolean value by comparing values and variables (see next page).