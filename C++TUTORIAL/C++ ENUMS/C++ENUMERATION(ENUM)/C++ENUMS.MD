C++ Enums
An enum is a special type that represents a group of constants (unchangeable values).

To create an enum, use the enum keyword, followed by the name of the enum, and separate the enum items with a comma:

enum Level {
  LOW,
  MEDIUM,
  HIGH
};
Note that the last item does not need a comma.

It is not required to use uppercase, but often considered as good practice.

Enum is short for "enumerations", which means "specifically listed".

To access the enum, you must create a variable of it.

Inside the main() method, specify the enum keyword, followed by the name of the enum (Level) and then the name of the enum variable (myVar in this example):

enum Level myVar;
Now that you have created an enum variable (myVar), you can assign a value to it.

The assigned value must be one of the items inside the enum (LOW, MEDIUM or HIGH):

enum Level myVar = MEDIUM;
By default, the first item (LOW) has the value 0, the second (MEDIUM) has the value 1, etc.

If you now try to print myVar, it will output 1, which represents MEDIUM:

int main() {
  // Create an enum variable and assign a value to it
  enum Level myVar = MEDIUM;

  // Print the enum variable
  cout << myVar;

  return 0;
}
Change Values
As you know, the first item of an enum has the value 0. The second has the value 1, and so on.

To make more sense of the values, you can easily change them:

enum Level {
  LOW = 25,
  MEDIUM = 50,
  HIGH = 75
};
int main() {
  enum Level myVar = MEDIUM;
  cout << myVar;  // Now outputs 50
  return 0;
}
Note that if you assign a value to one specific item, the next items will update their numbers accordingly:

enum Level {
  LOW = 5,
  MEDIUM, // Now 6
  HIGH // Now 7
};
Enum in a Switch Statement
Enums are often used in switch statements to check for corresponding values:

enum Level {
  LOW = 1,
  MEDIUM,
  HIGH
};

int main() {
  enum Level myVar = MEDIUM;

  switch (myVar) {
    case 1:
      printf("Low Level");
      break;
    case 2:
      printf("Medium level");
      break;
    case 3:
      printf("High level");
      break;
  }
  return 0;
}
Why And When To Use Enums?
Enums are used to give names to constants, which makes the code easier to read and maintain.

Use enums when you have values that you know aren't going to change, like month days, days, colors, deck of cards, etc.

