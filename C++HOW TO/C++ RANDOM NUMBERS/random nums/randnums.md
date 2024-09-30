Random Number  
You can use the rand() function, found in the <cstdlib> library, to generate a random number:  
  
Example  
cout << rand();  
To get more control over the random number, for example, if you only want a random number between 0 and 100, you can use the following formula:  
  
Example  
// Generate a random number between 0 and 100  
int randomNum = rand() % 101;  
  
cout << randomNum;  
return 0;  
Note: The examples above just outputs a random number once. They don't output different random numbers each time the program runs. To fix this, you can use the srand() function and add the time() function from the <ctime> library.  
  
This will generate a random number from 0 to 100 each time the program runs:  
  
Example  
// Get a different random number each time the program runs  
srand(time(0));  
  
// Generate a random number between 0 and 100  
int randomNum = rand() % 101;  
  
cout << randomNum;  
return 0;  
