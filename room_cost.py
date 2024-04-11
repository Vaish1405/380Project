from abc import abstractmethod

class Room():
    """Class for different types of rooms. 

    Attributes:
        roomType: The type of the room. (Standard or Deluxe or Super Deluxe)
    """ 
    def __init__(self, roomType):
        """Intializes the room object with given roomType

        Args:
            roomType: The type of the room.
        """
        self.roomType = roomType
    
    @abstractmethod
    def get_price(self):
        """Abstract method for the price of the room. 

        Returns:
            int: Room price for each type.
        """
        pass

class StandardRoom():
    """Class representing the standard room."""
    def get_price(self):
        """Get price of the Standard room.

        Returns:
            int: Prie of the Standard room.
        """
        return 109

class DeluxeRoom():
    """Class representing the Deluxe room."""
    def get_price(self):
        """Get price of the Deluxe room.

        Returns:
            int: Prie of the Deluxe room.
        """
        return 309

class SuperDeluxeRoom():
    """Class representing the Super Deluxe room."""
    def get_price(self):
        """Get price of the Super Deluxe room.

        Returns:
            int: Prie of the Super Deluxe room.
        """
        return 509
    
def get_room_price(selection):
    """Controller function to get the price of the room selected by the user.

    Args:
        selection: The type of room selected (Standard or Deluxe or Super Deluxe).

    Returns:
        int: The price of the selected room, or 0 if the selection is invalid.
    """
    selection = selection.lower()
    if selection == "standard":
        return StandardRoom().get_price()
    elif selection == "deluxe":
        return DeluxeRoom().get_price()
    elif selection == "superdeluxe":
        return SuperDeluxeRoom().get_price()
    else:
        return 0