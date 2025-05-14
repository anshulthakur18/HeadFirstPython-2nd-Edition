class CountFromBy:
    def __init(self, v: int=0, i: int=1)  -> None:
        self.val = v
        self.incr = i
    def increase(self)  -> None: 
        self.val += self.incr    #If you completely forget about it and fail to add it to your methods, amiss—the interpreter will display a slew of TypeErrors informing you that something is missing, and that something is self.
    def __repr__(self) -> str:
        return str(self.val)