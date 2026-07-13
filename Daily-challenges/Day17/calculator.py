'''Build a Calculator class.: Create methods for add(), subtract(),
multiply(), and divide() that accept two arguments and return the
result. Include basic error handling to prevent division by
zero.'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    
c1 = Calculator(4, 2)
print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())

