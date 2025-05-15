### Notes on Context Management Protocol

1. Context Management protocol dictates that any class you create must define at least two magic methods: `__enter__` and `__exit__`. A protocol is an agreed procedure (or set of rules) that is to be adhered to.

2. Dunder `__enter__` performs setup -> When an object is used with a `with` statement, the interpreter invokes the object’s `__enter__` method before the `with` statement’s suite starts. This provides an opportunity for you to perform any required setup code within dunder `__enter__`.

3. Dunder `__init__` initializes -> Defining dunder `__init__` lets you perform additional object initialization. Dunder `__init__` runs before `__enter__`.

4. Dunder `__exit__` does teardown -> As soon as the `with` statement’s suite ends, the interpreter always invokes the object’s `__exit__` method. This occurs after the `with` suite terminates, and it provides an opportunity for you to perform any required teardown.

5. If your class defines dunder `__enter__` and dunder `__exit__`, it’s a context manager.

6. When the interpreter encounters this `with` statement, it begins by calling any dunder `__init__` associated with the call to `open`:
  ```python
  with open('todos.txt') as tasks:
  ```
  - As soon as dunder `__init__` executes, the interpreter calls dunder `__enter__` to ensure that the result of calling `open` will be assigned to the `tasks` variable.
  - For example:
    ```python
    for chore in tasks:
      print(chore, end='')
    ```
  - When the `with` statement ends, the interpreter calls the context manager's dunder `__exit__` to tidy up. In this example, the interpreter ensures that the opened file is closed properly before continuing.
