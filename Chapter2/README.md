# Key Concepts of Python Objects

1. **Everything is an Object**  
  Everything is an object in Python, and any object can be assigned to a variable.

2. **State and Behavior**  
  Objects can have state (attributes or values) and behavior (methods).

3. **Built-in Data Structures**  
  Python comes with four built-in data structures that you can use to hold any collection of objects, and they are list, tuple, dictionary, and set.

# Lists in Python

4. **List Overview**  
  List: an ordered mutable collection of objects. Heterogeneous, dynamic (Can grow and shrink), and mutable. A list is like an array—the objects it stores are ordered sequentially in slots. Lists are always enclosed in square brackets, and the objects contained within the list are always separated by a comma.

5. **List Methods**  
  List methods: remove, pop, extend, and append.

  5.1. **remove**  
  Takes an object’s value as its sole argument. Removes the first occurrence of a specified data value from a list.

  5.2. **pop**  
  Takes an optional index value as its argument. The pop method removes and returns an object from an existing list based on the object’s index value.

  5.3. **extend**  
  Takes a list of objects as its sole argument. The extend method takes a second list and adds each of its objects to an existing list.

  5.4. **insert**  
  Takes an index value and an object as its arguments.

# Tuples in Python

6. **Tuple Overview**  
  When an ordered list-like collection is immutable (that is, it cannot change).

# Unordered Data Structures

7. **Unordered Data Structures**  

  7.1. **Dictionary**  
  An unordered set of key/value pairs. Unordered and mutable.

  7.2. **Set**  
  An unordered set of unique objects (while ensuring none of the objects are duplicated).

# Additional Notes on Lists

8. **Use Case for Lists**  
  Lists are great for storing a collection of related objects. If you have a bunch of similar things that you’d like to treat as one, a list is a great place to put them.

9. **Lists vs Arrays**  
  Lists are similar to arrays in other languages. However, unlike arrays in other languages (which tend to be fixed in size), Python’s lists can grow and shrink dynamically as needed.

10. **List Syntax**  
   In code, a list of objects is enclosed in square brackets, and the list objects are separated from each other by a comma.

11. **Empty List Representation**  
   An empty list is represented like this: [].

12. **Membership Check**  
   The fastest way to check whether an object is in a list is to use Python’s `in` operator, which checks for membership.

13. **Growing a List**  
   Growing a list at runtime is possible due to the inclusion of a handful of list methods, which include append, extend, and insert.

14. **Shrinking a List**  
   Shrinking a list at runtime is possible due to the inclusion of the remove and pop methods.

15. **Square Bracket Notation**  
   Lists understand the square bracket notation, which can be used to select individual objects from any list.

16. **Zero-based Indexing**  
   Like a lot of other programming languages, Python starts counting from zero, so the first object in any list is at index location 0, the second at 1, and so on.

17. **Negative Indexing**  
   Unlike a lot of other programming languages, Python lets you index into a list from either end. Using –1 selects the last item in the list, –2 the second last, and so on.

18. **List Slicing**  
   Lists also provide slices (or fragments) of a list by supporting the specification of start, stop, and step as part of the square bracket notation.

19. **Versatility of Lists**  
   Python lists are versatile and powerful for managing collections of data.