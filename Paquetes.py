from abc import ABC, abstractmethod


class Package(ABC):
    def __init__(self, id, code, description, gramsPrice, basePrice, weight, customer):
        self._id = id
        self._code = code
        self._description = description
        self._gramsPrice = gramsPrice
        self._basePrice = basePrice 
        self._weight = weight
        self._customer = customer
    
    def setId(self, id):
        self._id = id
        return self._id
    def getId(self, id):
        return self._id

    def calculate():
        return 1+1

class OverweightPackage(Package):
    def __init__(self, id, code, description, gramsPrice, basePrice, weight, customer,owerwight):
        super().__init__(id, code, description, gramsPrice, basePrice, weight, customer)
        self._owerwight = owerwight
    
    def calculate():
        return 1+1

class StandardPackage(Package):
    def __init__(self, id, code, description, gramsPrice, basePrice, weight, customer, quota):
        super().__init__(id, code, description, gramsPrice, basePrice, weight, customer)
        self._quota = quota
    def calculate():
        return 1+1



    
        