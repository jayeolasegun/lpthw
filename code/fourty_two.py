## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    pass

## ---  Dog is an instance of Animal
class Dog(Animal):

    def __init__(self, name):
        ## ---  Dog has a __init__ function with parameters self and name
        self.name = name


## ----  cat is an instance of Animal
class Cat(Animal):

    def __init__(self, name):
        ##  cat has a __init__ function with parameters self and name
        self.name = name


## ---  new class named Person is a object
class Person(object):

    def __init__(self, name):

        ## Person has a __init__ function with parameters self and name
        self.name = name

        ## Person has- a pet of some kind
        self.pet = None

## ---  Employee is an instance of Person
class Employee(Person):

    def __init__(self, name, salary):

        ## ?? hmm what is this strange magic?

        super(Employee, self).__init__(name)

        ##
        self.salary = salary


## ----  new class named Fish is a object
class Fish(object):

    pass


## ----   Salmon is an instance of Fish
class Salmon(Fish):
    pass


## ----   Halibut is an instance of Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a Dog
mary =  Person("Mary")

## mary has-a variable pet named satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

##  frank has-a variable pet named rover which is an object of Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon  --> Fish
crouse = Salmon()

## harry is-a Halibut --> Fish 
harry = Halibut()
