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

#### 2. How to make a script dynamic!

Write a program that prints the number of and the list of its arguments.

- The output should be:
  - Number of argument(s) followed by _argument_ (if number is one) or _arguments_ (otherwise), followed by
  - : (or . if no arguments were passed) followed by
  - a new line, followed by (if at least one argument),
  - one line per argument:
    - the position of the argument (starting at _1_) followed by :, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of _argv_ can be retrieved by using: _len(argv)_
- You do not have to fully understand lists yet, but imagine that _argv_ can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

#### 3. Infinite addition

Write a program that prints the result of the addition of all arguments

- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers by using _int()_ (you can assume that all arguments can be casted into integers)
- Your code should not be executed when imported

#### 4. Who are you?

Write a program that prints all the names defined by the compiled module _hidden_4.pyc_ (please download it locally).

- You should print one name per line, in alpha order
- You should print only names that do **not** start with __
-Your code should not be executed when imported
- Make sure you are running your code in Python3.8.x (_hidden_4.pyc_ has been compiled with this version)

#### 5. Everything can be imported

Write a program that imports the variable a from the file _variable_load_5.py_ and prints its value.

- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported
