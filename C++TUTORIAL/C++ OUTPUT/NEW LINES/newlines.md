New Lines
To insert a new line, you can use the \n character:

Example
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World! \n";
  cout << "I am learning C++";
  return 0;
}
You can also use another << operator and place the \n character after the text, like this:

Example
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!" << "\n";
  cout << "I am learning C++";
  return 0;
}
Tip: Two \n characters after each other will create a blank line:
Example
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!" << "\n\n";
  cout << "I am learning C++";
  return 0;
}
Another way to insert a new line, is with the endl manipulator:

#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!" << endl;
  cout << "I am learning C++";
  return 0;
}
Both \n and endl are used to break lines. However, \n is most used.

But what is \n exactly?
The newline character (\n) is called an escape sequence, and it forces the cursor to change its position to the beginning of the next line on the screen. This results in a new line.

Examples of other valid escape sequences are:
Escape Sequence	    |            Description
\t	                |            Creates a horizontal tab
\\                  |            Inserts a backslash character (\)	
\"	                |            Inserts a double quote character	
