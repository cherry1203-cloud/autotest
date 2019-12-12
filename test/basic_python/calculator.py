#计算器
import unittest2
class Calculator(unittest2.TestCase):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def plus(self):
        return self.a + self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a / self.b

if __name__ == '__main__':
    unittest2.main()