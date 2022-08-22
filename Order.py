import Paquetes
from enum import Enum

from .Person import Customer

#Clases de Ordenes 

class Location():
    def __init__(self, country, state, city, addresLine1, addresLine2, zipCode):
        self._country = country
        self._state = state 
        self._city = city
        self._addresLine1 = addresLine1
        self._addresLine2 = addresLine2
        self._zipCode = zipCode
    
    def setAddress(self, address):
        self._addresLine1 = address


class Order():
    def __init__(self, id: int, package: Paquetes.OverweightPackage or Paquetes.StandardPackage, paid: bool, price: float, receiver: Customer, sender: Customer, status, location: Location):
        self._id = id
        self._package = package,
        self._paid = paid, 
        self._price = price,
        self._receiver = receiver 
        self._sender = sender 
        self._status = status
        self._location = location 


class Invoice():
    def __init__(self, id, status, client, tax, price, discoint, paimentMethod, orders = []):
        self._id = id
        self._orders = orders 
        self._status = status 
        self._client = client 
        self._tax = tax 
        self._price = price,
        self._discoint = discoint 
        self._paimentMethod = paimentMethod


class Track():
    def __init__(self, id: int, type, maxWeight, currentWeight, status):
        self._id = id
        self._type = type
        self._maxWeight = maxWeight
        self._currentWeight = currentWeight
        self._status = status 

class Position():
    def __init__(self, lat, long):
        self._lat = lat 
        self._long = long



class Delivery():
    def __init__(self, status, track, internal, position, orders=[]):
        #CREATE DELIVERY OBJECT 
        self._orders = orders
        self._status = status 
        self._track = track
        self._driver = internal
        self._position = position
    
    def watchPosition(self):
        #RETURN POSITION 
        return self._position
    
    def getCurrentPosition(self):
        #RETURN CURRENT POSITION
        return self._position
    def setCurrentPosition(self, position):
        #CHANGE CURRENT POSITION
        self._position = position 
        
#ENUMERACIONES 

class OrderStatus(Enum):
    #CLASS FOR ORDER TYPES 
    PENDING = "PENDING"
    PAYMENT_DUE_DATE = "PAYMENT_DUE_DATE"

class InvoiceStatus(Enum):
    #CLASS FOR INVOICE TYPES 
    PROCESSING = "PROCESSING"
    SENT = "SENT"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"

class DeliveryStatus(Enum):
    #CLASS FOR DELIVERY TYPES
    DELIVERY = "DELIVERY"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"
    TRANSIT = "TRANSIT"
    PICKUO_AVALABLE = "PICKUO_AVALABLE"
    DELAYED = "DELAYED"
    DRAFTED = "DRAFTED"
class TrackType(Enum):
    #CLASS FOR TRACK TYPES 
    CAR = "CAR"
    TRUCK = "TRUCK"
    MOTORCYCLE= "MOTORCYCLE"
    BICYCLE = "BICYCLE"
    AIRPLANE = "AIRPLANE"

class TrackStatus(Enum):
    #CLASS FOR TRACK STATUS 
    IN_USE = "IN_USE"
    AVAILABLE = "AVAILABLE"
    MAINTENANCE = "MAINTENANCE"

class PaymentMethodsTypes(Enum):
    #CLASS FOR PAYMENT METHODS
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    TRANSFER = "TRANSFER"
    CASH = "CASH"