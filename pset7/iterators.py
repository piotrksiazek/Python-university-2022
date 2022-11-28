from itertools import cycle
import random

class IteratorZerosAndOnes:
    def toggle(self):
        self.num = 0 if self.num == 1 else 1
        return self.num

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        return self.toggle()
  
iteratorZerosAndOnes = IteratorZerosAndOnes()
zerosAndOnesIter = iter(iteratorZerosAndOnes)

for i in range(5):
    print(next(zerosAndOnesIter))

class IteratorRandomNESW:
    def __iter__(self):
        self.directions = ["N", "E", "W", "S"]
        return self

    def __next__(self):
        return random.choice(self.directions)
    
print("\n\n")    
    
iteratorRandomNESW = IteratorRandomNESW()
neswIter = iter(iteratorRandomNESW)

for i in range(10):
    print(next(neswIter))

class IteratorDaysOfWeek:
    def __iter__(self):
        self.days = cycle(list(range(7)))
        return self

    def __next__(self):
        return next(self.days)
    

print("\n\n") 
iteratorDays = IteratorDaysOfWeek()
daysIter = iter(iteratorDays)

for i in range(14):
    print(next(daysIter))