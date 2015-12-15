class Calc:   #Defining a class with name Calc
    def __init__(self, yes, no): #Class construction defining as a fun in class
        self.yes = yes
        self.no = no 

    def add(self): #defining  function add 2 numbers.
        return self.yes + self.no

    def mul(self):    #defining another function mul, multiplying two numbers
        return self.yes * self.no

newCalculation = Calc(10, 20)
print('a+b: %d' % newCalculation.add()) # Calling function from the class
print('a*b: %d' % newCalculation.mul())