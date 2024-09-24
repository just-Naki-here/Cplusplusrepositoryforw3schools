Real Life Example
To demonstrate a practical example of the while loop, we have created a simple "countdown" program:

Example
int countdown = 3;

while (countdown > 0) {
  cout << countdown << "\n";
  countdown--;
}

cout << "Happy New Year!!\n";
In this example, we create a program that only print even numbers between 0 and 10 (inclusive):

Example
int i = 0;

while (i <= 10) {
  cout << i << "\n";
  i += 2;
}
In this example we use a while loop to reverse some numbers:

Example
// A variable with some specific numbers
int numbers = 12345;

// A variable to store the reversed number
int revNumbers = 0;

// Reverse and reorder the numbers
while (numbers) {
  // Get the last number of 'numbers' and add it to 'revNumbers'
  revNumbers = revNumbers * 10 + numbers % 10;
  // Remove the last number of 'numbers'
  numbers /= 10;
}

cout << "Reversed numbers: " << revNumbers << "\n";
To demonstrate a practical example of the while loop combined with an if else statement, let's say we play a game of Yatzy:

Example
int dice = 1;

while (dice <= 6) {
  if (dice < 6) {
    cout << "No Yatzy\n";
  } else {
    cout << "Yatzy!\n";
  }
  dice = dice + 1;
}
If the loop passes the values ranging from 1 to 5, it prints "No Yatzy". Whenever it passes the value 6, it prints "Yatzy!".

