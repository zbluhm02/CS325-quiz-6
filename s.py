class Store:
    def __init__(self, info):
        self.info = info
    def iStore(self):
        print("Storing neccesary info from", self.info)

class Calc:
    def __init__(self, cost):
        self.cost = cost
    def math(self):
        print("Total cost is", self.cost * .125)

class Validate:
    def __init__(self, valid, data):
        self.valid = valid
        self.data = data
    def isValid(self):
        if (self.data==self.valid):
            return True

class Confirm:
    def __init__(self, confirmation, eAdress):
        self.confirmation = confirmation
        self.eAdress = eAdress
    def confirmEmail(self):
        print("Sending", self.confirmation, "to", self.eAdress)

class Inventory:
    def __init__(self, level):
        self.level = level
    def confirmEmail(self):
        self.level += self.level + 1
        return self.level
        

    