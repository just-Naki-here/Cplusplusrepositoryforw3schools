Omit Array Size
In C++, you don't have to specify the size of the array. The compiler is smart enough to determine the size of the array based on the number of inserted values:

string cars[] = {"Volvo", "BMW", "Ford"}; // Three array elements
The example above is equal to:

string cars[3] = {"Volvo", "BMW", "Ford"}; // Also three array elements
However, the last approach is considered as "good practice", because it will reduce the chance of errors in your program.

Omit Elements on Declaration
It is also possible to declare an array without specifying the elements on declaration, and add them later:

Example
string cars[5];
cars[0] = "Volvo";
cars[1] = "BMW";
cars[2] = "Ford";
cars[3] = "Mazda";
cars[4] = "Tesla";
Note: The example above only works when you have specified the size of the array.

If you don't specify the array size, an error occurs:

Example
string cars[];  // Array size is not specified
cars[0] = "Volvo";
cars[1] = "BMW";
cars[2] = "Ford";
cars[3] = "Mazda";
cars[4] = "Tesla";

// error: array size missing in 'cars'
Fixed Size (Arrays) vs. Dynamic Size (Vectors)
You will often hear the terms "fixed size" and "dynamic size" when discussing arrays in C++.

This is because the size of an array in C++ is fixed, meaning you cannot add or remove elements after it is created.

Arrays - Fixed Size Example
// An array with 3 elements
string cars[3] = {"Volvo", "BMW", "Ford"};

// Trying to add another element (a fourth element) to the cars array will result in an error
cars[3] = "Tesla";
Vectors
For operations that require adding and removing array elements, C++ provides vectors, which are resizable arrays.

The size of a vector is dynamic, meaning it can grow and shrink as needed.

Vectors are found in the <vector> library, and they come with many useful functions to add, remove and modify elements:

Vectors - Dynamic Size Example
// A vector with 3 elements
vector<string> cars = {"Volvo", "BMW", "Ford"};

// Adding another element to the vector
cars.push_back("Tesla");
This was just an introduction to vectors to let you know that "resizable arrays" exist.

Don't worry if you don't understand the syntax above.

You will learn much more about vectors and other data structures in a later chapter.