C++ Deque
In the previous page, your learned that elements in a queue are added at the end and removed from the front.

A deque (stands for double-ended queue) however, is more flexible, as elements can be added and removed from both ends (at the front and the back). You can also access elements by index numbers.

To use a deque, you have to include the <deque> header file:

// Include the deque library
#include <deque>
Create a Deque
To create a deque, use the deque keyword, and specify the type of values it should store within angle brackets <> and then the name of the deque, like: deque<type> dequeName.

Example
// Create a deque called cars that will store strings
deque<string> cars;
If you want to add elements at the time of declaration, place them in a comma-separated list, inside curly braces {}:

Example
// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Print deque elements
for (string car : cars) {
  cout << car << "\n";
}
Note: The type of the deque (string in our example) cannot be changed after its been declared.

Access a Deque
You can access a deque element by referring to the index number inside square brackets [].

Deques are 0-indexed, meaning that [0] is the first element, [1] is the second element, and so on:

Example
// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars[0];  // Outputs Volvo

// Get the second element
cout << cars[1];  // Outputs BMW
You can also access the first or the last element of a deque with the .front() and .back() functions:

Example
// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the first element
cout << cars.front();

// Get the last element
cout << cars.back();
To access an element at a specified index, you can use the .at() function and specify the index number:

Example
// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Get the second element
cout << cars.at(1);

// Get the third element
cout << cars.at(2);
Note: The .at() function is often preferred over square brackets [] because it throws an error message if the element is out of range:

Example
// Create a deque called cars that will store strings
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Try to access an element that does not exist (will throw an exception)
cout << cars.at(6);
Change a Deque Element
To change the value of a specific element, you can refer to the index number:

Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Change the value of the first element
cars[0] = "Opel";

cout << cars[0];  // Now outputs Opel instead of Volvo
However, it is safer to use the .at() function:

Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Change the value of the first element
cars.at(0) = "Opel";

cout << cars.at(0);  // Now outputs Opel instead of Volvo
Add Deque Elements
To add elements to a deque, you can use .push_front() to insert an element at the beginning of the deque and .push_back() to add an element at the end:

Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Add an element at the beginning
cars.push_front("Tesla");

// Add an element at the end
cars.push_back("VW");
Remove Deque Elements
To remove elements from a deque, use .pop_front() to remove an element from the beginning of the deque and .pop_back() to remove an element at the end:

Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Remove the first element
cars.pop_front();

// Remove the last element
cars.pop_back();
Deque Size
To find out how many elements a deque has, use the .size() function:

Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cout << cars.size();  // Outputs 4
Check if a Deque is Empty
Use the .empty() function to find out if a deque is empty or not.

The .empty() function returns 1 (true) if the deque is empty and 0 (false) otherwise:

Example
deque<string> cars;
cout << cars.empty();  // Outputs 1 (The deque is empty)
Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cout << cars.empty();  // Outputs 0 (not empty)
Loop Through a Deque
You can loop through the deque elements by using a for loop combined with the .size() function:

Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (int i = 0; i < cars.size(); i++) {
  cout << cars[i] << "\n";
}
You can also use a for-each loop (introduced in C++ version 11 (2011), which is cleaner and more readable:

Example
deque<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (string car : cars) {
  cout << car << "\n";
}
Tip: It is also possible to loop through deques with an iterator, which you will learn more about in a later chapter.