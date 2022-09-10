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
- You can only use the word _add_0_ once in your code
- You are not allowed to use * for importing or **import**
- Your code should not be executed when imported - by using **import**, like the example below

#### 1. My first toolbox!

Write a program that imports functions from the file _calculator_1.py_, does some Maths, and prints the result.

- Do not use the function _print_ (with string format to display integers) more than 4 times
- You have to define:
  - the value _10_ to a variable _a_
  - the value _5_ to a variable _b_
- and use those two variables only, as arguments when calling functions (including _print)
- _a_ and _b_ must be defined in 2 different lines: _a = 10_ and another _b = 5_
- Your program should call each of the imported functions. See example below for format
- the word _calculator_1_ should be used only once in your file
- You are not allowed to use _*_ for importing or __import__
- Your code should not be executed when imported
