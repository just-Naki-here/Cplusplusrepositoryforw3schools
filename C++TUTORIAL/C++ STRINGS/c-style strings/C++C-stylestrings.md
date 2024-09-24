C-Style Strings
C-style strings are created with the char type instead of string.

The name comes from the C language, which, unlike many other programming languages, does not have a string type for easily creating string variables. Instead, you must use the char type and create an array of characters to make a "string" in C.

As C++ was developed as an extension of C, it continued to support this way of creating strings in C++:

Example
string greeting1 = "Hello";  // Regular String
char greeting2[] = "Hello";  // C-Style String (an array of characters)

Note: It is more convenient to work with the standard string type, rather than C-style strings. However, one reason some users continue to use C-style strings is that they have access to functions from the C standard library.

A list of all C-style string functions, can be found in the c++ reference folder
