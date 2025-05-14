class CountFromBy:
    def __init(self, v: int, i: int)  -> None:
        self.val = v
        self.incr = i
    def increase(self)  -> None: 
        self.val += self.incr

a = CountFromBY() # () creates an object by appending the parenthesisto the class name, then assign the newly created object to a variable

b = CountFromBY()

# Doing More with CountFromBy
c = CountFromBY() # CountFromBY()  object starts at 0 and in increments by 1
print(c)
c.increase()
c.increase()
c.increase()
print(c)

d = CountFromBY(100) ## CountFromBY()  object starts at 100 and in increments by 1
print(d)
d.increase()
d.increase()
d.increase()
print(d)

e = CountFromBY(100,10) # Amount to increase by 10
print(e)
for i in range(3):
    e.increase()
print(e)


f = CountFromBY(incremnet=15) #Object increment by 15
print(f)

for j in range(3):
    f.increase()
print(f)

h = CountFromBY(100, 10) #Object increment by 10
print(h.value)
print(h.incr)
print(h.increase())
print(h) # hexadecimal value which is the memory address of the object
#Override dunder “repr” to specify how your objects are represented by the interpreter.
def __repr__(self) -> str:
    return str(self)





