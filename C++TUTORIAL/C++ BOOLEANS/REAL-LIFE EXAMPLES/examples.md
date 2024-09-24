Real Life Example
Let's think of a "real life example" where we need to find out if a person is old enough to vote.

In the example below, we use the >= comparison operator to find out if the age (25) is greater than OR equal to the voting age limit, which is set to 18:

Example
int myAge = 25;
int votingAge = 18;

cout << (myAge >= votingAge); // returns 1 (true), meaning 25 year olds are allowed to vote!

Cool, right? An even better approach (since we are on a roll now), would be to wrap the code above in an if...else statement, so we can perform different actions depending on the result:

Example
Output "Old enough to vote!" if myAge is greater than or equal to 18. Otherwise output "Not old enough to vote.":

int myAge = 25;
int votingAge = 18;

if (myAge >= votingAge) {
  cout << "Old enough to vote!";
} else {
  cout << "Not old enough to vote.";
}

// Outputs: Old enough to vote!
Booleans are the basis for all C++ comparisons and conditions.

You will learn more about conditions (if...else) in the next chapter.