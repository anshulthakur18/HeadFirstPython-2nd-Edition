1. **Functions introduce two new keywords:** `def` and `return`.

2. **The `def` keyword** names the function and details any arguments the function may have. The use of the `return` keyword is optional and is used to pass back a value to the code that invoked the function.

3. **Functions can accept argument data.** Functions contain code and (usually) documentation.

4. **Triple quotes around strings** are known as docstrings.

5. **Strings enclosed by a single quote character (`'`) or a double quote character (`"`)** cannot span multiple lines: you must terminate the string with a matching quote character on the same line (as Python uses the end of the line as a statement terminator).

6. **Annotations, also known as hints.** Function annotations are optional and informational.

7. **Functions are named chunks of code.** The `def` keyword is used to name a function, with the function’s code indented under (and relative to) the `def` keyword.

8. **Python’s triple-quoted strings** can be used to add multiline comments to a function. When they are used in this way, they are known as docstrings.

9. **Functions can accept any number of named arguments,** including none.

10. **The `return` statement** lets your functions return any number of values (including none).

11. **Function annotations** can be used to document the type of your function’s arguments, as well as its return type.

12. **As well as assigning arguments by position,** you can use keywords, too. When you do, any ordering is acceptable (as any possibility of ambiguity is removed by the use of keywords and position doesn’t matter anymore).

13. **The three main locations the interpreter searches when looking for a module:**
  - Your current working directory
  - Your interpreter's site-packages locations
  - The standard library locations

14. **A module** is one or more functions saved in a file.

15. **You can share a module** by ensuring it is always available with the interpreter’s current working directory (which is possible, but brittle) or within the interpreter’s site-packages locations (by far the better choice).

16. **Following the `setuptools` three-step process** ensures that your module is installed into site-packages, which allows you to import the module and use its functions no matter what your current working directory happens to be.

17. **Python’s function argument semantics** support both call-by-value and call-by-reference. The interpreter looks at the type of the value referred to by the object reference (the memory address) and, if the variable refers to a mutable value, call-by-reference semantics apply. If the type of the data referred to is immutable, call-by-value semantics kick in.

18. **Strings, integers, and tuples (being immutable)** are always passed into a function by value.
