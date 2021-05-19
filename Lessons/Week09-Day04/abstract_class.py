from abc import ABC, abstractmethod
 
class Car(ABC):
 
    @abstractmethod
    def model(self):
        pass
 
class Porshce(Car):
 
    def model(self):
        print("Porshce")
 
class Mercedes(Car):
 
    def model(self):
        print("Mercedes")
 
class BMW(Car):
 
    def model(self):
        print("BMW")
 
class Tesla(Car):
 
    def model(self):
        print("Tesla")
 
# Driver code
R = Porshce()
R.model()
 
K = Mercedes()
K.model()
 
R = BMW()
R.model()
 
K = Tesla()
K.model()




# Python program showing
# abstract base class work
 
from abc import ABC, abstractmethod
class Animal(ABC):
 
    def move(self):
        pass
 

 
class Snake(Animal):
 
    def move(self):
        print("I can crawl")
 
class Dog(Animal):
 
    def move(self):
        print("I can bark")
 
class Lion(Animal):
 
    def move(self):
        print("I can roar")
         

K = Snake()
K.move()
 
R = Dog()
R.move()
 
K = Lion()
K.move()