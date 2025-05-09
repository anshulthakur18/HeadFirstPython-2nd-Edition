1. Everything is an object in Python, and any object can be assigned to a variable.

2. Objects can have state (attributes or values) and behavior (methods).

3. Python comes with four built-in data structures that you can use to hold any collection of objects, and they are list, tuple, dictionary, and set.

4. List: an ordered mutable collection of objects. Heterogeneous, dynamic (Can grow and shrink), and mutable. A list is like an array—the objects it stores are ordered sequentially in slots. Lists are always enclosed in square brackets, and the objects contained within the list are always separated by a comma.

5. List methods: remove, pop, extend, and append

  5.1. remove: takes an object’s value as its sole argument. Removes the first occurrence of a specified data value from a list.
  5.2. pop: takes an optional index value as its argument. The pop method removes and returns an object from an existing list based on the object’s index value.
  5.3. extend: takes a list of objects as its sole argument. The extend method takes a second list and adds each of its objects to an existing list.
  5.4. insert: takes an index value and an object as its arguments.

6. Tuple: When an ordered list-like collection is immutable (that is, it cannot change).

7. Two unordered data structures:

  7.1. Dictionary: an unordered set of key/value pairs. Unordered and mutable.
  7.2. Set: an unordered set of unique objects (while ensuring none of the objects are duplicated).

8. Lists are great for storing a collection of related objects. If you have a bunch of similar things that you’d like to treat as one, a list is a great place to put them.

9. Lists are similar to arrays in other languages. However, unlike arrays in other languages (which tend to be fixed in size), Python’s lists can grow and shrink dynamically as needed.

10. In code, a list of objects is enclosed in square brackets, and the list objects are separated from each other by a comma.

11. An empty list is represented like this: [].

12. The fastest way to check whether an object is in a list is to use Python’s in operator, which checks for membership.

13. Growing a list at runtime is possible due to the inclusion of a handful of list methods, which include append, extend, and insert.

14. Shrinking a list at runtime is possible due to the inclusion of the remove and pop methods.

15. Lists understand the square bracket notation, which can be used to select individual objects from any list.

16. Like a lot of other programming languages, Python starts counting from zero, so the first object in any list is at index location 0, the second at 1, and so on.

17. Unlike a lot of other programming languages, Python lets you index into a list from either end. Using –1 selects the last item in the list, –2 the second last, and so on.

18. Lists also provide slices (or fragments) of a list by supporting the specification of start, stop, and step as part of the square bracket notation.

19. Python lists are versatile and powerful for managing collections of data.