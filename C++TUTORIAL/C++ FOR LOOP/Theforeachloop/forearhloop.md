The foreach Loop
There is also a "for-each loop" (also known as ranged-based for loop), which is used exclusively to loop through elements in an [array] [or other data structures]:

Syntax
for (type variableName : arrayName) {
  // code block to be executed
}
The following example outputs all elements in an array, using a "for-each loop":

Example
int myNumbers[5] = {10, 20, 30, 40, 50};
for (int i : myNumbers) {
  cout << i << "\n";
}
Note: Don't worry if you don't understand the example above. You will learn more about arrays in the C++ Arrays chapter.

Good to know: The for-each loop was introduced in C++ version 11 (2011).