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
'''
import logging

def write_file(fill_path , data):
    try:
        with open(fill_path , "w") as file:
            file.write(data)
    except Exception as e:
        pass
logging.basicConfig(level = logging.DEBUG ,
                    filename = "info.txt" ,
                    filemode = "w" ,
                    format = '%(asctime)s - %(levelname)s - %(message)s')
write_file("info.txt" , input("Введіть будь що і я виведу це в окремий файл:"))

'''
#3

import random
import logging

def rand_file(file_path , num):
    try:
        with open(file_path , "w") as file:
            for i in range(num):
                data = random.randint(1,10)
                file.write(str(data) + '\n')
                logging.info(f"Рандомне число: {data}")
    except Exception as e:
        logging.error(f"Помилка: {e}")

rand_file("numbers.txt" , int(input("Кількість згенерованих чисел: ")))






