Parameters and Arguments
Information can be passed to functions as a parameter. Parameters act as variables inside the function.

Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma:

Syntax
void functionName(parameter1, parameter2, parameter3) {
  // code to be executed
}
The following example has a function that takes a string called fname as parameter. When the function is called, we pass along a first name, which is used inside the function to print the full name:

Example
void myFunction(string fname) {
  cout << fname << " Refsnes\n";
}

int main() {
  myFunction("Liam");
  myFunction("Jenny");
  myFunction("Anja");
  return 0;
}

// Liam Refsnes
// Jenny Refsnes
// Anja Refsnes
When a parameter is passed to the function, it is called an argument. So, from the example above: fname is a parameter, while Liam, Jenny and Anja are arguments.