vowels = set('aieou')
word = input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word)) #a combination of the objects in both sets (a union):
for vowel in found:
    print(vowel)
