from abc import ABC 
from Order import Location

class Person(ABC):
    def __init__(self, id , nationalid, idType, personType, name, email, lastName, location, validation = False):
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

class PersonManager():
    def __init__(self, customers = [], internals = []):
        self._customers = customers 
        self._internals = internals
    
    def addPerson(self, typeOfPerson):
        id = int(input("ingresar ID: "))
        nationalid = input("Ingresar nacionalidad")
        idType = input("Tipo de identificacion: ")
        personType = input("Tipo de persona: LEGAL - NATURAL")
        name = input("Nombre: ")
        lastName = input("Apellido: ")
        email = input("Email: ")
        country = input("pais: ")
        state = input("Estado: ")
        city = input("Ciudad: ")
        addresLine1 = input("Linea1 de comunicacion: ")
        addresLine2 = input("Linea2 de comunicacion: ") 
        zipCode = input("ZipCode: ")      
        location = Location(country, state, city, addresLine1, addresLine2, zipCode)
        if typeOfPerson == 1:
            newCustomer = Customer(id, nationalid, idType, personType, name, email, lastName, location, validation = False)
        else:
            role = input("Role: ")
            accountId = input("Account ID: ")
            bankId = input("BankId: ")
            bankName = input("Bank Name: ")
            newBankAccount = BankAccount(accountId, bankName, bankId)
            newInternal = Internal(id, nationalid, idType, personType, name, email, lastName, location, role, newBankAccount, validation = False)


class Customer(Person):
    def __init__(self, id, nationalid, idType, personType, name, email, lastName, location, validation = False, invoices = [], creditCard = [], shipping = [],):
        super().__init__(id, nationalid, idType, personType, name, email, lastName, location, validation = False)
        self._creditCard = creditCard
        self._invoices = invoices
        self._shipping = shipping
    
    def addCreditCard(self):
        cvv = int(input("cvv: "))
        number = int(input("number: "))
        expiryYear = int(input("año de expiracion: "))
        expiryMonth = int(input("mes de expiracion: "))
        zipCode = int(input("zipCode: "))


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
