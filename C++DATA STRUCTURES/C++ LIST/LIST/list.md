C++ List
A list is similar to a vector in that it can store multiple elements of the same type and dynamically grow in size.

However, two major differences between lists and vectors are:

You can add and remove elements from both the beginning and at the end of a list, while vectors are generally optimized for adding and removing at the end.

Unlike vectors, a list does not support random access, meaning you cannot directly jump to a specific index, or access elements by index numbers.
To use a list, you have to include the <list> header file:

// Include the list library
#include <list>
Create a List
To create a list, use the list keyword, and specify the type of values it should store within angle brackets <> and then the name of the list, like: list<type> listName.

Example
// Create a list called cars that will store strings
list<string> cars;
If you want to add elements at the time of declaration, place them in a comma-separated list, inside curly braces {}:

Example
// Create a list called cars that will store strings
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Print list elements
for (string car : cars) {
  cout << car << "\n";
}
Note: The type of the list (string in our example) cannot be changed after its been declared.

Access a List
You cannot access list elements by referring to index numbers, like with arrays and vectors.

However, you can access the first or the last element with the .front() and .back() functions, respectively:

Example
// Create a list called cars that will store strings
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars.front();  // Outputs Volvo

// Get the last element
cout << cars.back();  // Outputs Mazda
Change a List Element
You can also change the value of the first or the last element with the .front() and .back() functions

Example
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Change the value of the first element
cars.front() = "Opel";

// Change the value of the last element
cars.back() = "Toyota";

cout << cars.front(); // Now outputs Opel instead of Volvo
cout << cars.back();  // Now outputs Toyota instead of Mazda
Add List Elements
To add elements to a list, you can use .push_front() to insert an element at the beginning of the list and .push_back() to add an element at the end:

Example
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Add an element at the beginning
cars.push_front("Tesla");

// Add an element at the end
cars.push_back("VW");
Remove List Elements
To remove elements from a list, use .pop_front() to remove an element from the beginning of the list and .pop_back() to remove an element at the end:

Example
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Remove the first element
cars.pop_front();

// Remove the last element
cars.pop_back();
List Size
To find out how many elements a list has, use the .size() function:

Example
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cout << cars.size();  // Outputs 4
Check if a List is Empty
Use the .empty() function to find out if a list is empty or not.

The .empty() function returns 1 (true) if the list is empty and 0 (false) otherwise:

Example
list<string> cars;
cout << cars.empty();  // Outputs 1 (The list is empty)
Example
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cout << cars.empty();  // Outputs 0 (not empty)
Loop Through a List
You cannot loop through the list elements with a traditional for loop combined with the .size() function, since it is not possible to access elements in a list by index:

Example
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (int i = 0; i < cars.size(); i++) {
  cout << cars[i] << "\n";
}
The simplest way to loop through a list is with the for-each loop:

Example
list<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (string car : cars) {
  cout << car << "\n";
}
Tip: It is also possible to loop through lists with an iterator, which you will learn more about in a later chapter.