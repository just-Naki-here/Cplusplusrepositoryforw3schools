C++ Output (Print Text)
The cout object, together with the << operator, is used to output values/print text:

Example
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}
You can add as many cout objects as you want. However, note that it does not insert a new line at the end of the output:

Example
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  cout << "I am learning C++";
  return 0;
}
