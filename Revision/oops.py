class Car:
    def start(self):
        print('car is starting')
car1=Car()
car1.start()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
s1=Student('keerthi',21)
s1.display()

