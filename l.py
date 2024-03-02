from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        raise NotImplementedError("Subclass didn't implemnt area funct") #Error throwing with python is much much better than C++ in my opinion
    @abstractmethod
    def set_dimensions(self, *args):
        raise NotImplementedError("Subclass didn't implement dimension funct.")
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def set_dimensions(self, base, height):
        self.base = base
        self.height = height
        #Subclasses should work in superclass so LSP shouldn't be violated. My superclass might be to general though so that could be improved.