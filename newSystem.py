class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *=2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


# Abstraction = the repair of the podracer does not specifically say how it was repaired, just that it is

# Encapulation = The Podracer class wrapped the __init__ and repair together

# Inheritance = The AnakinsPod class and SebulbasPod Class both used the Podracer class 

# Polymorphism = It showed different ways to adjust the condition of the Podracer

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not? 
# Answer: No because OOP is already the easiest method for this simple problem 

# How in particular did Object Oriented Programming assist in the solving of this problem?
# Answer: OOP allows the problem to be more maintainable and extensible