#from curses import halfdelay

class MathDojo:

    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result+=num
        for i in nums:
            self.result+=i
        return self
    
    def subtract(self, num, *nums):
        self.result-=num
        for i in nums:
            self.result-=i
        return self

md = MathDojo()
mf = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result # should print 5
print(x)

y = mf.add(2).add(5,5,5).subtract(5,5).result
print(y)

mf.result=0

y = mf.add(10,5,5).add(2,4,1).add(9,12,4).result
print(y)

mf.result=0

y = mf.subtract(10,5,10).subtract(10,1,5).subtract(12,4,3).result
print(y)

mf.result=0

y= mf.add(10,10,10,10,10).add(50).add(25,25).subtract(10,20,20).subtract(10).subtract(10,10,10,20).result
print(y)
# run each of the methods a few more times and check the result!

