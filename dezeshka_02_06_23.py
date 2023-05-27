#1

import logging

class StudentProcessor:
     def __init__(self):
      self.students = []
      self.logger = logging.getLogger("StudentProcessor")
      self.logger.setLevel(logging.INFO)
      self.logger.addHandler(logging.StreamHandler())
     def add_student(self,student):
       self.students.append(student)
       self.logger.info(f"{student} was added to students")
     def remove_student(self,student):
       self.students.remove(student)
       if student in self.students:
        self.logger.info(f"{student} was removed from students")
       else:
        print("Student wasn't found in our database")
     def process_students(self,student):
         for student in self.students:
                self.logger.info("Processing is in progress...")

dima = StudentProcessor()
dima.add_student("Dima")

kolya = StudentProcessor()
kolya.add_student("Kolya")

filip = StudentProcessor()
filip.add_student("Filip")

masha = StudentProcessor()
masha.add_student("Masha")

dima = StudentProcessor()
dima.remove_student("Dima")