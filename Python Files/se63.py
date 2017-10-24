class Animal(object):

    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        

hippo = Animal("Sam", 3)

hippo.description()
print hippo.is_alive


class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)
my_car.display_car()

class Represent(object):
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    def __repr__(self):
        return ("His name is %s. He is %s years old and he lives in %s") % (
            self.name, self.age, self.location)

tomy = Represent("Tomy", 16, "Byala Slatina")
print tomy
print tomy.name,
print tomy.age,
print tomy.location
