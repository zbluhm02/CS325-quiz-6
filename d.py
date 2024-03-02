from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class SpecificLogger(Logger):
    def log (self,message):
        print("Specific code written for a specifc logger here.")
        #Allows the code to reference the class as opposed to the specific syntax of the included function.