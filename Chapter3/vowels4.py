# Common use case senario is to perform a frequency count. The sorted built-in function can be used for sorting of data.
# Dictionaries have a bunch of built-in methods, and one of these is the items method, which returns a list of the key/value pairs. Using items with for is often the preferred technique for iterating over a dictionary, as it gives you access to the key and the value as loop variables, which you can then use in your suite.

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provde a word to search for vowels: ")
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
  if letter in vowels:
    found[letter] += 1
for k,v in sorted(found.items()):
  print(k, 'was found', v, 'time(s).')