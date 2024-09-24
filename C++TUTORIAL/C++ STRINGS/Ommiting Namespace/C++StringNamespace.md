Omitting Namespace
You might see some C++ programs that run without the standard namespace library. The using namespace std line can be omitted and replaced with the std keyword, followed by the :: operator for string (and cout) objects:

Example
#include <iostream>
#include <string>
// using namespace std; - Remove this line

int main() {
  std::string greeting = "Hello";
  std::cout << greeting;
  return 0;
}

It is up to you if you want to include the standard namespace library or not.

In our tutorial, we will continue to include the library.