Real Life Example
To demonstrate a practical example of using functions, let's create a program that converts a value from fahrenheit to celsius:

Example
// Function to convert Fahrenheit to Celsius
float toCelsius(float fahrenheit) {
  return (5.0 / 9.0) * (fahrenheit - 32.0);
}

int main() {
  // Set a fahrenheit value
  float f_value = 98.8;

  // Call the function with the fahrenheit value
  float result = toCelsius(f_value);

  // Print the fahrenheit value
  cout << "Fahrenheit: " << f_value << "\n";

  // Print the result
  cout << "Convert Fahrenheit to Celsius: " << result << "\n";

  return 0;
}