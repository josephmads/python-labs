# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Snake():
    
    def __init__(self, length, fangs) -> None:
        self.length = length
        self.fangs = fangs

class Lizard(Snake):
    
    def __init__(self, length, fangs, claws) -> None:
        super().__init__(length, fangs)
        self.claws = claws

class Dragon(Lizard):
    
    def __init__(self, length, fangs, claws, wings) -> None:
        super().__init__(length, fangs, claws)
        self.wings = wings