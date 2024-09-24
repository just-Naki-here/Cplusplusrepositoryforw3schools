String Concatenation
The + operator can be used between strings to add them together to make a new string. This is called concatenation:

Example
string firstName = "John ";
string lastName = "Doe";
string fullName = firstName + lastName;
cout << fullName;
In the example above, we added a space after firstName to create a space between John and Doe on output. However, you could also add a space with quotes (" " or ' '):

Example
string firstName = "John";
string lastName = "Doe";
string fullName = firstName + " " + lastName;
cout << fullName;

Append
A string in C++ is actually an object, which contain functions that can perform certain operations on strings. For example, you can also concatenate strings with the append() function:

Example
string firstName = "John ";
string lastName = "Doe";
string fullName = firstName.append(lastName);
cout << fullName;
Tip: A list of other useful string functions, can be found in the C++ reference folder