# AirBnB Clone Group Project- Cohort 14

## Description

### Complete a clone of the AirBnB web application, composed of:
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)rimester as well as learni  ng a few new concepts as we work on this project.

![](https://images-na.ssl-images-amazon.com/images/I/91YRBwPbutL.png)

## Requirements

### Python Scripts
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file, at the root of the folder of the project, is mandatory
6. Your code should use the PEP 8 style (version 1.7 or more)
7. All your files must be executable
8. The length of your files will be tested using wc
9. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
10. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
11. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and p    ython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
12. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be    verified)

### Python Unit Tests
1. Allowed editors: vi, vim, emacs
2. All your files should end with a new line
3. All your test files should be inside a folder tests
4. You have to use the unittest module
5. All your test files should be python files (extension: .py)
6. All your test files and folders should start by test_
7. Your file organization in the tests folder should be the same as your project
   e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
   e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
8. All your tests should be executed by using this command: python3 -m unittest discover tests
9. You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
10. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
11. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
12. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and p   ython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
13. We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Execution
Your shell should work like this in interactive mode:

````
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
````

But also in non-interactive mode: (like the Shell project in C)

````
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
````

All tests should also pass in non-interactive mode:
~~~~~~
$ echo "python3 -m unittest discover tests" | bash
~~~~~~

### Resources

* [Python Packages](https://intranet.hbtn.io/concepts/66)
* [AirBnB clone](https://intranet.hbtn.io/concepts/74)
* [HBNB Project Overview](https://www.youtube.com/watch?v=E12Xc3H2xqo)
* [HBNB- The Console](https://www.youtube.com/watch?v=p00ES-5K4C8)
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

### Contributors

1. Bree Browder - 2372@holbertonschool.com
3. Nikki Edmonds - 2495@holbertonschool.com

```
Project Due Date: May 25, 2021
```