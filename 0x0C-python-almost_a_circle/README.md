## Python - Almost a circle

# Tasks

**0. If it's not tested it doesn't work**

All your files, classes and methods must be unit tested and be PEP 8 validated.

**1. Base class**

Write the first class _Base_:

Create a folder named **models** with an empty file **__init__.py** inside - with this file, the folder will become a Python package

Create a file named **models/base.py**:

- Class **Base**:
  - private class attribute _*__nb_objects = 0**_
  - class constructor: **def __init__(self, id=None):**:
    - if **id** is not **None**, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
