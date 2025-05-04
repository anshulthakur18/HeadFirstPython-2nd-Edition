prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prices.remove(5)
print(prices)
prices.remove(6)
print(prices)
prices.pop()
print(prices)
prices.pop(-3) 
#Python extends the notation to improve upon this standardized behavior by supporting negative index values
#positive index values count from left to right(from 0), whereas negative index values count from right to left(from -1)
print(prices)
prices.pop(2)
print(prices)
prices.extend([11, 12, 13])
print(prices)
prices.insert(2,3)
print(prices)
prices.insert(4,5)
print(prices)
prices.insert(5,6)
print(prices)


# care need to be taken when working with list such as reference
first = [1, 2, 3, 4, 5]
print(first)
second = first
print(second)
second.append(6)
print(first)
# both first and second are pointing to the same data. If you change one list, the other changes, too. This is not good.

# To avoid this, you can use the copy() method to create a new list that is a copy of the original list.

third = first.copy()
third.append(7)
print(third)
print(first)

#Lists Understand Start, Stop, and Step similar to range(). Slicing a List Is Nondestructive
print(prices)
print(prices[0:12:2]) # start at 0, stop at 12, step by 2
print(prices[2:])
print(prices[:10])
print(prices[::3])

#string to list and vice versa
book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
print(''.join(booklist[0:3]))
print(''.join(booklist[-6:]))