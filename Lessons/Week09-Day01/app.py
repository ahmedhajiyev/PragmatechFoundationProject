class Main():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print(f'Name: {self.name}\nAge: {self.age}')

main1 = Main('Ahmed', 20)
main1.func()

class Car():
    def __init__(self, model, type):
        self.model = model
        self.type = type

    def func(self):
        print(f'Model: {self.model}\nType: {self.type}')

car1 = Car('Volvo', 'SUV')
car1.func()

class Electric(Car):
    def __init__(self, model, type):
        super().__init__(model, type)
    def func(self):
        print(f'Model: {self.model}\nType: {self.type}')

car2 = Electric('Tesla', 'Sedan')
car2.func()


class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def func(self):
        print('Name: ' + self.fname + '\n' + 'Surname: ' + self.lname)

person1 = Person('Namiq', 'Faracov')
person1.func()


class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def print(self):
         print('Name: ' + self.fname + '\n' + 'Surname: ' + self.lname + '\n' + 'Age: ' + f'{self.age}')

student1 = Student('Ramiz', 'Yunusov', 15)
student1.print()


class Animals:
    def __init__(self, name):
        self.name = name
    def reaction(self):
        print('ERROR')
class Cat(Animals):
    def reaction(self):
        return 'Miyav!'
class Dog(Animals):
    def reaction(self):
        return 'Haav! Hav!'

animal = [Cat('Mestan'),
           Cat('Simpa'),
           Dog('Alabas')]
for hyvn in animal:
    print(hyvn.name + ': ' + hyvn.reaction())



class Car():
    def __init__(self, model, type, km):
        self.model = model
        self.type = type
        self.km = km

    def func(self):
        print(f'Model: {self.model}\nType: {self.type}\nKm: {self.km}' )


    def change_odemeter(self, new_km):
        self.km += new_km

car1 = Car('Volvo', 'SUV', 500)
car1.func()
