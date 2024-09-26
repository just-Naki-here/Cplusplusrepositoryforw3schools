C++ Stack
A stack stores multiple elements in a specific order, called LIFO.

LIFO stands for Last in, First Out. To vizualise LIFO, think of a pile of pancakes, where pancakes are both added and removed from the top. So when removing a pancake, it will always be the last one you added. This way of organizing elements is called LIFO in computer science and programming.

Unlike vectors, elements in the stack are not accessed by index numbers. Since elements are added and removed from the top, you can only access the element at the top of the stack.

To use a stack, you have to include the <stack> header file:

// Include the stack library
#include <stack>
Create a Stack
To create a stack, use the stack keyword, and specify the type of values it should store within angle brackets <> and then the name of the stack, like: stack<type> stackName.

// Create a stack of strings called cars
stack<string> cars;
Note: The type of the stack (string in our example) cannot be changed after its been declared.

Note: You cannot add elements to the stack at the time of declaration, like you can with vectors:

stack<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
Add Elements
To add elements to the stack, use the .push() function, after declaring the stack:

Example
// Create a stack of strings called cars
stack<string> cars;

// Add elements to the stack
cars.push("Volvo");
cars.push("BMW");
cars.push("Ford");
cars.push("Mazda");
The stack will look like this (remember that the last element added is the top element):

Mazda (top element)
Ford
BMW
Volvo
Access Stack Elements
You cannot access stack elements by referring to index numbers, like you would with arrays and vectors.

In a stack, you can only access the top element, which is done using the .top() function:

Example
// Access the top element
cout << cars.top();  // Outputs "Mazda"
Change the Top Element
You can also use the .top function to change the value of the top element:

Example
// Change the value of the top element
cars.top() = "Tesla";

 // Access the top element
cout << cars.top();  // Now outputs "Tesla" instead of "Mazda"
Remove Elements
You can use the .pop() function to remove an element from the stack.

This will remove the last element that was added to the stack:

Example
// Create a stack of strings called cars
stack<string> cars;

// Add elements to the stack
cars.push("Volvo");
cars.push("BMW");
cars.push("Ford");
cars.push("Mazda");

// Remove the last added element (Mazda)
cars.pop();

// Access the top element (Now Ford)
cout << cars.top();
Get the Size of the Stack
To find out how many elements a stack has, use the .size() function:

Example
cout << cars.size();
Check if the Stack is Empty
Use the .empty() function to find out if the stack is empty or not.

The .empty() function returns 1 (true) if the stack is empty and 0 (false) otherwise:

Example
stack<string> cars;
cout << cars.empty(); // Outputs 1 (The stack is empty)
Example
stack<string> cars;

cars.push("Volvo");
cars.push("BMW");
cars.push("Ford");
cars.push("Mazda");

cout << cars.empty();  // Outputs 0 (not empty)
Stacks and Queues
Stacks are often mentioned together with Queues, which is a similar data structure described on the next page.

