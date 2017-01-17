# A methodical Approach
# prints name and age using my defined function within the class
# then prints the health of each animal

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Big Guy", 3)

hippo.description()

sloth = Animal("Lazy", 10)

ocelot = Animal("Cutie", 2)

print hippo.health
print sloth.health
print ocelot.health
