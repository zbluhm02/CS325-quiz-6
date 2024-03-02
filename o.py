from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        area = self._calculate_area()
        print("The area is:", area)
        return area

    @abstractmethod
    def _calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def _calculate_area(self):
        return self.side ** 2
    
    def get_area(self):
        return super().get_area() #Not entirly sure why this works but it does, I need to do more research on this later.
    #You should be able to add new shops without modifying existing code in base class Shape.