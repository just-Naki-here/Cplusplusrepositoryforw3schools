Real Life Example
This example shows how you can use if..else to "open a door" if the user enters the correct code:

Example
int doorCode = 1337;

if (doorCode == 1337) {
  cout << "Correct code.\nThe door is now open.\n";
} else {
  cout << "Wrong code.\nThe door remains closed.\n";
}
This example shows how you can use if..else to find out if a number is positive or negative:

Example
int myNum = 10; // Is this a positive or negative number?

if (myNum > 0) {
  cout << "The value is a positive number.\n";
} else if (myNum < 0) {
  cout << "The value is a negative number.\n";
} else {
  cout << "The value is 0.\n";
}
Find out if a person is old enough to vote:

Example
int myNum = 10; // Is this a positive or negative number?

if (myNum > 0) {
  cout << "The value is a positive number.\n";
} else if (myNum < 0) {
  cout << "The value is a negative number.\n";
} else {
  cout << "The value is 0.\n";
}
Find out if a number is even or odd:

Example
int myNum = 5;

if (myNum % 2 == 0) {
  cout << myNum << " is even.\n";
} else {
  cout << myNum << " is odd.\n";
}