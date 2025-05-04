''' 
if 'bananas' in fruits:
  fruits['bananas'] += 1
else:
  fruits['bananas'] = 1

=> another way to write the above code is:
  if 'bananas' not in fruits:
    fruits['bananas'] = 0
  fruits['bananas'] += 1

  => another way to write the above code is using setdeafult method:
  fruits.setdefault('bananas', 0)
  fruits['bananas'] += 1
'''

# Upadtion of the code

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provde a word to search for vowels: ")

found = {}

for letter in word:
  if letter in vowels:
    found.setdefault(letter, 0) #know setdefault’s behavior is guaranteed to initialize a nonexistent key to a supplied default value, or to do nothing
    found[letter] += 1 #Use “setdefault” to help avoid the “KeyError” exception.


for k,v in sorted(found.items()):
  print(k, 'was found', v, 'time(s).')