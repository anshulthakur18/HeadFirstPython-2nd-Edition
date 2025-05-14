# Understanding Classes in Python

1. **Classes and Objects**
  - Classes let you bundle behavior and state together in an object.
  - Define a class's behavior by creating methods.
    - **Behavior**: Think of it as a function, a chunk of code that does something.
    - **State**: Think of it as variables, a place to store values within a class.

2. **Object Instantiation**
  - Invoke a class to create an object.

3. **Defining a Class**
  ```
  # A class starts with the "class" keyword followed by the class name.
  class CountFromBy:
     pass
  # “pass” is a valid statement (i.e., it is syntactically correct), but it does nothing. Think of it as an empty statement.
  ```

4. **Behavior and State**
  - Objects share behavior but not state.
    - When you create objects from a class, each object shares the class’s coded behaviors (the methods defined in the class) but maintains its own copy of any state (the attributes).
  - Class behavior is shared by each of its objects, whereas state is not. Each object maintains its own state.

5. **Calling Methods**
  - Example: `c.increase()` where `c` is the object and `increase()` is the name of the method.
  - Alternatively: `CountFromBy.increase(c)` where:
    - `CountFromBy` is the name of the class within which the method is defined.
    - `increase` is the name of the method.
    - `(c)` is the object (to increase).

6. **The `self` Argument**
  - Each method’s first argument has a special name: `self`.
  - When writing code in a class, think of `self` as an alias to the current object.

7. **Creating Objects**
  - The `class` keyword introduces a new class in your code.
  - Creating a new object from a class looks very much like a function call.
    - Example: To create an object called `mycount` from a class called `CountFromBy`, you’d use this line of code:
     ```python
     mycount = CountFromBy()
     ```

8. **Shared Code and Attributes**
  - When an object is created from a class:
    - The object shares the class’s code with every other object created from the class.
    - However, each object maintains its own copy of the attributes.

9. **Adding Behaviors**
  - You add behaviors to a class by creating methods.
  - A method is a function defined within a class.

10. **Adding Attributes**
   - To add an attribute to a class, create a variable.

11. **The `self` Prefix**
   - Every method is passed an alias to the current object as its first argument.
   - Python convention insists that this first argument is called `self`.
   - Within a method’s suite, referrals to attributes are prefixed with `self`, ensuring the attribute’s value survives after the method code ends.

12. **The `__init__` Method**
   - The `__init__` method is one of the many magic methods provided with all Python classes.
   - Attribute values are initialized by the `__init__` method (a.k.a. dunder init).
   - This method lets you assign starting values to your attributes when a new object is created.
   - Example:
    ```python
    mycount2 = CountFromBy(100, 10)
    ```
    - Here, the values `100` and `10` are passed into `__init__` when this object is created.

13. **The `__repr__` Method**
   - Another magic method is `__repr__`, which allows you to...
