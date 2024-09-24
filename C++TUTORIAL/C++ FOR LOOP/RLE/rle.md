Real Life Example
To demonstrate a practical example of the for loop, let's create a program that counts to 100 by tens:

Example
for (int i = 0; i <= 100; i += 10) {
  cout << i << "\n";
}
In this example, we create a program that only print even numbers between 0 and 10 (inclusive):

Example
for (int i = 0; i <= 10; i = i + 2) {
  cout << i << "\n";
}
Here we only print odd numbers:

Example
for (int i = 1; i <= 10; i = i + 2) {
  cout << i << "\n";
}
In this example we print the powers of 2 up to 512:

Example
for (int i = 2; i <= 512; i *= 2) {
  cout << i << "\n";
}
And in this example, we create a program that prints the multiplication table for a specified number:

Example
int number = 2;
int i;

// Print the multiplication table for the number 2
for (i = 1; i <= 10; i++) {
  cout << number << " x " << i << " = " << number * i << "\n";
}