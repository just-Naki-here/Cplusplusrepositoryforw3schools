# C++ Map

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
- [Example 13](#example-13)
- [Example 14](#example-14)
- [Example 15](#example-15)
- [Example 16](#example-16)
- [Example 17](#example-17)
- [Example 18](#example-18)

## Overview

A map stores elements in "key/value" pairs.

Elements in a map are:

Accessible by keys (not index), and each key is unique.
Automatically sorted in ascending order by their keys.
To use a map, you have to include the <map> header file:

// Include the map library
#include <map>
Create a Map
To create a map, use the map keyword, and specify the type of both the key and the value it should store within angle brackets <>. At last, specify the name of the map, like: map<keytype, valuetype> mapName:

## Example 1

```cpp
// Create a map called people that will store strings as keys and integers as values
```

map<string, int> people
If you want to add elements at the time of declaration, place them in a comma-separated list, inside curly braces {}:

## Example 2

```cpp
// Create a map that will store the name and age of different people
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };
```

Access a Map
You cannot access map elements by referring to index numbers, like you would with arrays and vectors.

Instead, you can access a map element by referring to its key inside square brackets []:

## Example 3

```cpp
// Create a map that will store the name and age of different people
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Get the value associated with the key "John"
cout << "John is: " << people["John"] << "\n";

// Get the value associated with the key "Adele"
cout << "Adele is: " << people["Adele"] << "\n";
```

You can also access elements with the .at() function:

## Example 4

```cpp
// Create a map that will store the name and age of different people
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Get the value associated with the key "Adele"
cout << "Adele is: " << people.at("Adele") << "\n";

// Get the value associated with the key "Bo"
cout << "Bo is: " << people.at("Bo") << "\n";
```

Note: The .at() function is often preferred over square brackets [] because it throws an error message if the element does not exist:

## Example 5

```cpp
// Create a map that will store the name and age of different people
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Try to access an element that does not exist (will throw an exception)
cout << people.at("Jenny");
```

Change Values
You can also change the value associated with a key:

## Example 6

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Change John's value to 50 instead of 32
people["John"] = 50;

cout << "John is: " << people["John"]; // Now outputs John is: 50
```

However, it is safer to use the .at() function:

## Example 7

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Change John's value to 50 instead of 32
people.at("John") = 50;

cout << "John is: " << people.at("John"); // Now outputs John is: 50
```

Add Elements
To add elements to a map, it is ok to use square brackets []:

## Example 8

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Add new elements
people["Jenny"] = 22;
people["Liam"] = 24;
people["Kasper"] = 20;
people["Anja"] = 30;
```

But you can also use the .insert() function:

## Example 9

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Add new elements
people.insert({"Jenny", 22});
people.insert({"Liam", 24});
people.insert({"Kasper", 20});
people.insert({"Anja", 30});
```

Elements with Equal Keys
A map cannot have elements with equal keys.

For example, if we try to add "Jenny" two times to the map, it will only keep the first one:

## Example 10

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Trying to add two elements with equal keys
people.insert({"Jenny", 22});
people.insert({"Jenny", 30});
```

To sum up; values can be equal, but keys must be unique.

Remove Elements
To remove specific elements from a map, you can use the .erase() function:

## Example 11

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Remove an element by key
people.erase("John");
```

To remove all elements from a set, you can use the .clear() function:

## Example 12

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

// Remove all elements
people.clear();
```

Find the Size of a Map
To find out how many elements a map has, use the .size() function:

## Example 13

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };
cout << people.size(); // Outputs 3
```

Check if a Map is Empty
Use the .empty() function to find out if a map is empty or not.

The .empty() function returns 1 (true) if the map is empty and 0 (false) otherwise:

## Example 14

```cpp
map<string, int> people;
cout << people.empty(); // Outputs 1 (The map is empty)
```

## Example 15

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };
cout << people.empty(); // Outputs 0 (not empty)
```

Note: You can also check if a specific element exists, by using the .count(key) function.

It returns 1 (true) if the element exists and 0 (false) otherwise:

## Example 16

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };
cout << people.count("John"); // Outputs 1 (John exists)
```

Loop Through a Map
You can loop through a map with the for-each loop. However, there are a couple of things to be aware of:

You should use the auto keyword (introduced in C++ version 11) inside the for loop. This allows the compiler to automatically determine the correct data type for each key-value pair.
Since map elements consist of both keys and values, you have to include .first to access the keys, and .second to access values in the loop.
Elements in the map are sorted automatically in ascending order by their keys:
## Example 17

```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

for (auto person : people) {
cout << person.first << " is: " << person.second << "\n";
}
```

The output will be:

Adele is: 45
Bo is: 29
John is: 32
If you want to reverse the order, you can use the greater<type> functor inside the angle brackets, like this:

## Example 18

```cpp
map<string, int, greater<string>> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} };

for (auto person : people) {
cout << person.first << " is: " << person.second << "\n";
}
```

The output will be:

John is: 32
Bo is: 29
Adele is: 45
Tip: It is also possible to loop through maps with an iterator, which you will learn more about in the next chapter.
