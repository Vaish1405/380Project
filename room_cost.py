from abc import abstractmethod

class Room(): 
    def __init__(self, roomType):
        self.roomType = roomType
    
    @abstractmethod
    def get_price(self):
        pass

class StandardRoom():
    def get_price(self):
        return 109

class DeluxeRoom():
    def get_price(self):
        return 309

class SuperDeluxeRoom():
    def get_price(self):
        return 509
    
def get_room_price(selection):
    selection = selection.lower()
    if selection == "standard":
        return StandardRoom().get_price()
    elif selection == "deluxe":
        return DeluxeRoom().get_price()
    elif selection == "superdeluxe":
        return SuperDeluxeRoom().get_price()
    else:
        return 0