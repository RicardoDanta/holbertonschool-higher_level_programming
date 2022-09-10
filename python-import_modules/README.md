## Python: Import & Modules

### General Learning Objetives:

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function _dir()_
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

### Tasks

#### 0. Import a simple function from a simple file

Write a program that imports the function **def add(a, b)**: from the file _add_0.py_ and prints the result of the addition **1 + 2 = 3**

- You have to use _print_ function with string format to display integers
- You have to assign:
  - the value _1_ to a variable called _a_
  - the value _2_ to a variable called _b_
  - and use those two variables as arguments when calling the functions _add_ and _print_
- _a_ and _b_ must be defined in 2 different lines: _a = 1_ and another _b = 2_
- Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
- You can only use the word _add_0_ once in your code
- You are not allowed to use * for importing or **import**
- Your code should not be executed when imported - by using **import**, like the example below
