from abc import ABC 

class Person(ABC):
    def __init__(self, id, nationalid, idType, personType, name, email, lastName, location, validation = False):
        self._id = id
        self._nationalid = nationalid
        self._idType = idType
        self._personType = personType
        self._name = name
        self._email = email
        self._lastName = lastName 
        self._location = location
        self._validation = validation
        
    def biometricValidation(self):
        self.validation = True


class Customer(Person):
    def __init__(self, id, nationalid, idType, personType, name, email, lastName, location, validation = False, invoices = [], creditCard = [], shipping = [],):
        super().__init__(id, nationalid, idType, personType, name, email, lastName, location, validation = False)
        self._creditCard = creditCard
        self._invoices = invoices
        self._shipping = shipping

class Internal(Person):
    def __init__(self, id, nationalid, idType, personType, name, email, lastName, location, role, account, validation = False, invoices = [], creditCard = [], shipping = [],):
        super().__init__(id, nationalid, idType, personType, name, email, lastName, location, validation = False)
        self._role = role
        self._account = account 

class CreditCard():
    def __init__(self, cvv, expiryYear, expiryMonth, expiryDate, number, zipCode):
        self._cvv = cvv 
        self._expiryYear = expiryYear 
        self._expiryMonth = expiryMonth 
        self._expiryDate = expiryDate
        self._number = number 
        self._zipCode = zipCode

    def validation():
        return False

class BankAccount():
    def __init__(self, accountId, bankName, bankId, balance = 0.0):
        self._accountId = accountId
        self._bankName = bankName
        self._bankId = bankId
        self._balance = balance

    def deposit(self, ammount):
        self._deposit += ammount
        return self._deposit
