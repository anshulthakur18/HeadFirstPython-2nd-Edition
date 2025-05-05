# Creating a dictionary with keys and values
person3 = {'Name': 'Ford Prefect',
           'Gender': 'Male',
           'Occupation': 'Researcher',
           'Home Planet': 'Betelgeuse Seven' }

print(person3)
print(person3['Name'])

# Add a new key-value pair to the dictionary

person3['Age'] = 33
print(person3)

# Set example

vowels = set('aeiou')
word = 'hello'
u = vowels.union(set(word)) #a combination of the objects in both sets (a union):
print(u)
u_list = list(u) #convert the set to a list
print(u_list)
#The difference function compares the objects in vowels against the objects in set(word), then returns a new set of objects (called d here) which are in the vowels set but not in set(word).
d = vowels.difference(set(word))
print(d)
#The intersection function compares the objects in vowels against the objects in set(word), then returns a new set of objects (called i here) which are in both sets.
i = vowels.intersection(set(word))
print(i)

#TUPLE example

'''
vowels = ('a', 'e', 'i', 'o', 'u')
type(vowels)
print(vowels)
vowels[2] = 'A' #TypeError: 'tuple' object does not support item assignment
'''

#store a single string in a tuple.

t = ('Python')
print(type(t))
print(t)

#In order for a tuple to be a tuple, every tuple needs to include at least one comma between the parentheses, even when the tuple contains a single object.

t2 = ('Python',)
print(type(t2))
print(t2)

#complex built-in data types
#list, tuple, set, and dictionary are all complex built-in data types. They are called complex because they can contain other objects, including other complex objects. The simplest of these is the list, which is a collection of objects that can be of any type. Lists are mutable, meaning you can change them after they are created. Tuples are similar to lists, but they are immutable, meaning you cannot change them after they are created. Sets are unordered collections of unique objects. Dictionaries are collections of key-value pairs.

people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven' }

people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth'}

people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home Planet': 'Earth'}

people['Robot'] = {'Name': 'Marvin',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home Planet': 'Unknown'}

print(people) # interpreter will dump the entire dictionary to the screen

#Python standord library has a built-in module called pprint, which stands for pretty print. This module provides a way to format the output of complex data structures in a more readable way.

import pprint
pprint.pprint(people)

#accessing data in a complex data structure

print(people['Ford']['Name']) # Ford Prefect
print(people['Trillian']['Home Planet']) # Earth
