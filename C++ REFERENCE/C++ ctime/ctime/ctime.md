C++ ctime Functions
The <ctime> library has a variety of functions that allow you to measure dates and times.

| Function    | Description                                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------------------|
| asctime()   | Returns a C-style string representation of the time in a tm structure                                         |
| clock()     | Returns a number representing the amount of time that has passed while the program is running                 |
| ctime()     | Returns a C-style string representation of the time in a timestamp                                            |
| difftime()  | Returns the time difference between two timestamps                                                            |
| gmtime()    | Converts a timestamp into a tm structure representing its time at the GMT time zone                           |
| localtime() | Converts a timestamp into a tm structure representing its time in the system's local time zone                |
| mktime()    | Converts a tm structure into a timestamp                                                                      |
| strftime()  | Writes a C-style string representing the date and time of a tm structure with a variety of formatting options |
| time()      | Returns a timestamp representing the current moment in time                                                   |