

class Order():
    def __init__(self, id, package, paid, price, receiver, sender, status, location):
        self._id = id
        self._package = package,
        self._paid = paid, 
        self._price = price,
        self._receiver = receiver 
        self._sender = sender 
        self._status = status
        self._location = location 


class Invoice():
    def __init__(self, id, orders, status, client, tax, price, discoint, paimentMethod):
        self._id = id
        self._orders = orders 
        self._status = status 
        self._client = client 
        self._tax = tax 
        self._price = price,
        self._discoint = discoint 
        self._paimentMethod = paimentMethod


class Track():
    def __init__(self, id, type, maxWeight, currentWeight, status):
        self._id = id
        self._type = type
        self._maxWeight = maxWeight
        self._currentWeight = currentWeight
        self._status = status 

class Position():
    def __init__(self, lat, long):
        self._lat = lat 
        self._long = long

class Location():
    def __init__(self, country, state, city, addresLine1, addresLine2, zipCode):
        self._country = country
        self._state = state 
        self._city = city
        self._addresLine1 = addresLine1
        self._addresLine2 = addresLine2
        self._zipCode = zipCode
    


class Delivery():
    def __init__(self, status, track, internal, position, orders=[]):
        self._orders = orders
        self._status = status 
        self._track = track
        self._driver = internal
        self._position = position
    
    def watchPosition(self):
        return self._position
    
    def getCurrentPosition(self):
        return self._position
    def setCurrentPosition(self, position):
        self._position = position 
        
