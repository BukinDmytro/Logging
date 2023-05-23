#1
import logging
'''

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add(self,a,b):
        result = a + b
        self.logger.info(f"{a} + {b} = {result}")
        return result
    def substract(self,a,b):
        result = a - b
        self.logger.info(f"{a} - {b} = {result}")
        return result
    def multiply(self,a,b):
        result = a * b
        self.logger.info(f"{a} * {b} = {result}")
        return result
    def divide(self,a,b):
        if b != 0:
            result = a / b
            self.logger.info(f"{a} / {b} = {result}")
            return result
        else:
            raise ValueError("Division by zero buddy !!!")


a = Calculator()
a.divide(8,4)

'''
#2





