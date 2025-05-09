# Python Data Structures Overview

## 1. Dictionaries

1. **Definition**: A dictionary (also known as an associative array, map, hash, or table) is used to hold a collection of key/value pairs.

2. **Key/Value Structure**:
  - Each key is enclosed in quotes (as they are strings), as is each value.
  - Keys and values don’t have to be strings, however.
  - Each key is separated from its associated value by a colon (`:`).
  - Each key/value pair (a.k.a. “row”) is separated from the next by a comma.

3. **Accessing Data**:
  - Like lists, dictionaries use square bracket notation.
  - Unlike lists, dictionaries use keys (not numeric indices) to access their associated values.
  - Example: `person3['Name']`.

4. **Structure**:
  - Think of a dictionary as a collection of rows, with each row containing exactly two columns:
    - The first column stores a key.
    - The second column contains a value.

5. **Dynamic Nature**:
  - Dictionaries can grow and shrink on demand.
  - Each row is known as a key/value pair, and a dictionary can contain any number of key/value pairs.

6. **Syntax**:
  - A dictionary is enclosed in curly braces `{}`.
  - Each key/value pair is separated from the next by a comma.
  - Each key is separated from its value by a colon.

7. **Order**:
  - Insertion order is not maintained by a dictionary.
  - The order in which rows are inserted has no bearing on how they are stored.

8. **Accessing Values**:
  - Use square bracket notation to access values.
  - Example: `dictionary[key]`.

9. **Iteration**:
  - Python’s `for` loop can iterate over a dictionary.
  - On each iteration, the key is assigned to the loop variable, which can be used to access the associated value.

10. **Sorting**:
   - By default, dictionaries are unordered.
   - Use the `sorted` built-in function to sort a dictionary on output.

11. **`items` Method**:
   - The `items` method allows iteration over a dictionary by row (key/value pair).
   - On each iteration, the `items` method returns the next key and its associated value.

12. **Error Handling**:
   - Accessing a nonexistent key results in a `KeyError`, causing a runtime error.

13. **Avoiding `KeyError`**:
   - Ensure every key in your dictionary has a value before accessing it.
   - Use the `in` and `not in` operators or the `setdefault` method to avoid errors.

---

## 2. Sets

14. **Definition**: A collection of objects separated by commas and surrounded by curly braces `{}`.
   - Example: `{'a', 'e', 'i', 'o', 'u'}`.

15. **Set Operations**:
   - Sets can perform set-like operations such as difference, intersection, and union.

16. **Uniqueness**:
   - Sets do not allow duplicate elements.

17. **Syntax**:
   - Like dictionaries, sets are enclosed in curly braces `{}`.
   - However, sets do not identify key/value pairs.
   - Each unique object in the set is separated by a comma.

18. **Order**:
   - Sets do not maintain insertion order.
   - Use the `sorted` function to order a set.

19. **Creating Sets**:
   - Pass any sequence to the `set` function to create a set of elements from the sequence (duplicates are removed).

20. **Built-in Functionality**:
   - Sets include methods to perform union, difference, and intersection.

---

## 3. Tuples

21. **Immutability**:
   - Tuples are immutable, meaning they cannot be changed after creation.

---

## 4. General Notes

22. **Nested Structures**:
   - Built-in data structures can store other built-in data structures.
   - This is possible because everything in Python is an object.

23. **Rich Functionality**:
   - Python provides a rich set of built-in data structures to handle various use cases efficiently.
