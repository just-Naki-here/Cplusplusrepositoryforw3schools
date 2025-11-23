# C++ Set

## Table of Contents

- [Overview](#overview)
- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)
- [Example 4](#example-4)
- [Example 5](#example-5)
- [Example 6](#example-6)
- [Example 7](#example-7)
- [Example 8](#example-8)
- [Example 9](#example-9)
- [Example 10](#example-10)
- [Example 11](#example-11)
- [Example 12](#example-12)

## Overview

A set stores unique elements where they:

Are sorted automatically in ascending order.
Are unique, meaning equal or duplicate values are ignored.
Can be added or removed, but the value of an existing element cannot be changed.
Cannot be accessed by index numbers, because the order is based on sorting and not indexing.
To use a set, you have to include the <set> header file:

// Include the set library
#include <set>
Create a Set
To create a set, use the set keyword, and specify the type of values it should store within angle brackets <> and then the name of the set, like: set<type> setName.

## Example 1

```cpp
// Create a set called cars that will store strings
set<string> cars;
```

If you want to add elements at the time of declaration, place them in a comma-separated list, inside curly braces {}:

## Example 2

```cpp
// Create a set called cars that will store strings
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Print set elements
for (string car : cars) {
cout << car << "\n";
}
```

The output will be:

BMW
Ford
Mazda
Volvo
As you can see from the result above, the elements in the set are sorted automatically. In this case, alphabetically, as we are working with strings.

If you store integers in the set, the returned values are sorted numerically:

## Example 3

```cpp
// Create a set called numbers that will store integers
set<int> numbers = {1, 7, 3, 2, 5, 9};

// Print set elements
for (int num : numbers) {
cout << num << "\n";
}
```

The output will be:

1
2
3
5
7
9
Note: The type of the set (e.g. string and int in the examples above) cannot be changed after its been declared.

Sort a Set in Descending Order
By default, the elements in a set are sorted in ascending order. If you want to reverse the order, you can use the greater<type> functor inside the angle brackets, like this:

## Example 4

```cpp
// Sort elements in a set in descending order
set<int, greater<int>> numbers = {1, 7, 3, 2, 5, 9};
// Print the elements
for (int num : numbers) {
cout << num << "\n";
}
```

The output will be:

9
7
5
3
2
1
Note: The type specified in greater<type> must match the type of elements in the set (int in our example).

Unique Elements
Elements in a set are unique, which means they cannot be duplicated or equal.

For example, if we try to add "BMW" two times in the set, the duplicate element is ignored:

## Example 5

```cpp
set<string> cars = {"Volvo", "BMW", "Ford", "BMW", "Mazda"};

// Print set elements
for (string car : cars) {
cout << car << "\n";
}
```

The output will be:

BMW
Ford
Mazda
Volvo
Add Elements
To add elements to a set, you can use the .insert() function:

## Example 6

```cpp
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Add new elements
cars.insert("Tesla");
cars.insert("VW");
cars.insert("Toyota");
cars.insert("Audi");
```

Remove Elements
To remove specific elements from a set, you can use the .erase() function:

## Example 7

```cpp
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Remove elements
cars.erase("Volvo");
cars.erase("Mazda");
```

To remove all elements from a set, you can use the .clear() function:

## Example 8

```cpp
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

// Remove all elements
cars.clear();
```

Find the Size of a Set
To find out how many elements a set has, use the .size() function:

## Example 9

```cpp
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cout << cars.size(); // Outputs 4
```

Check if a Set is Empty
Use the .empty() function to find out if a set is empty or not.

The .empty() function returns 1 (true) if the set is empty and 0 (false) otherwise:

## Example 10

```cpp
set<string> cars;
cout << cars.empty(); // Outputs 1 (The set is empty)
```

## Example 11

```cpp
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
cout << cars.empty(); // Outputs 0 (not empty)
```

Loop Through a Set
You can loop through a set with the for-each loop:

## Example 12

```cpp
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};

for (string car : cars) {
cout << car << "\n";
}
```

Tip: It is also possible to loop through sets with an iterator, which you will learn more about in a later chapter.
