1. **IDLE and Command Line**  
  1.1. IDLE, Python’s built-in IDE, is used to experiment with and execute Python code, either as single-statement snippets or as larger multistatement programs written within IDLE’s text editor.  
  1.2. As well as using IDLE, you ran a file of Python code directly from your operating system’s command line, using the `py -3` command (on Windows) or `python3` (on everything else).  

2. **Data Types**  
  2.1. You’ve learned how Python supports single-value data items, such as integers and strings, as well as the booleans `True` and `False`.  

3. **Built-in Data Structures**  
  3.1. You’ve explored use cases for the four built-in data structures: lists, dictionaries, sets, and tuples.  
  3.2. You know that you can create complex data structures by combining these four built-ins in any number of ways.  

4. **Python Statements**  
  4.1. You’ve used a collection of Python statements, including `if`, `elif`, `else`, `return`, `for`, `from`, and `import`.  

5. **Standard Library Modules**  
  5.1. You know that Python provides a rich standard library, and you’ve seen the following modules in action: `datetime`, `random`, `sys`, `os`, `time`, `html`, `pprint`, `setuptools`, and `pip`.  

6. **Built-in Functions (BIFs)**  
  6.1. As well as the standard library, Python comes with a handy collection of built-in functions, known as the BIFs.  
  6.2. Here are some of the BIFs you’ve worked with: `print`, `dir`, `help`, `range`, `list`, `len`, `input`, `sorted`, `dict`, `set`, `tuple`, and `type`.  

7. **Operators**  
  7.1. Python supports all the usual operators, and then some.  
  7.2. Those you’ve already seen include: `in`, `not in`, `+`, `-`, `=` (assignment), `==` (equality), `+=`, and `*`.  

8. **Sequence Notation and Slicing**  
  8.1. As well as supporting the square bracket notation for working with items in a sequence (i.e., `[]`), Python extends the notation to support slices, which allow you to specify start, stop, and step values.  

9. **Custom Functions**  
  9.1. You’ve learned how to create your own custom functions in Python, using the `def` statement.  
  9.2. Python functions can optionally accept any number of arguments as well as return a value.  

10. **String Conventions**  
   10.1. Although it’s possible to enclose strings in either single or double quotes, the Python conventions (documented in PEP 8) suggest picking one style and sticking to it.  
   10.2. For this book, we’ve decided to enclose all of our strings within single quotes, unless the string we’re quoting itself contains a single quote character, in which case we’ll use double quotes (as a one-off, special case).  

11. **Triple-Quoted Strings**  
   11.1. Triple-quoted strings are also supported, and you’ve seen how they are used to add docstrings to your custom functions.  

12. **Modules and Code Reuse**  
   12.1. You learned that you can group related functions into modules.  
   12.2. Modules form the basis of the code reuse mechanism in Python, and you’ve seen how the `pip` module (included in the standard library) lets you consistently manage your module installations.  

13. **Everything is an Object**  
   13.1. Speaking of things working in a consistent manner, you learned that in Python everything is an object, which ensures—as much as possible—that everything works just as you expect it to.  
   13.2. This concept really pays off when you start to define your own custom objects using classes, which we’ll show you how to do in a later chapter.  

14. **The `__name__` Value**  
   14.1. The `__name__` value is maintained by the Python interpreter and, when used anywhere within your program’s code, identifies the currently active module.  
   14.2. “Dunder name” is shorthand for the same thing.  

15. **Decorators**  
   15.1. The `@` symbol before a function’s name identifies it as a decorator.  
   15.2. Decorators let you change the behavior of an existing function without having to change the function’s code.  
   15.3. Although decorators can also be applied to classes as well as functions, they are mainly applied to functions, which results in most Python programmers referring to them as function decorators.  
   15.4. In your webapp, you used Flask’s `@app.route` decorator to associate URLs with Python functions.  
   15.5. A function can be decorated more than once (as you saw with the `entry_page` function).  

16. **HTTP Status Codes**  
   16.1. The various HTTP status codes that can be sent from a web server. There are five main categories of status code:  
      16.1.1. Codes in the 100–199 range are informational messages: all is OK, and the server is providing details related to the client’s request.  
      16.1.2. Codes in the 200–299 range are success messages: the server has received, understood, and processed the client’s request. All is good.  
      16.1.3. Codes in the 300–399 range are redirection messages: the server is informing the client that the request can be handled elsewhere.  
      16.1.4. Codes in the 400–499 range are client error messages: the server received a request from the client that it does not understand and can’t process. Typically, the client is at fault here.  
      16.1.5. Codes in the 500–599 range are server error messages: the server received a request from the client, but the server failed while trying to process it. Typically, the server is at fault here.  

17. **Python Package Index (PyPI)**  
   17.1. You learned about the Python Package Index (PyPI), which is a centralized repository for third-party Python modules.  
   17.2. When connected to the Internet, you can automatically install packages from PyPI using `pip`.  
   17.3. You used `pip` to install the Flask micro-web framework, which you then used to build your webapp.  

18. **Jinja2 Template Engine**  
   18.1. You learned how to use the Jinja2 text template engine to render HTML pages from within your webapp.  
