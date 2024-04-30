from .Room import Room

class SuperDeluxeRoom(Room):
    """
    Programmer: Vaishnavi Sen

    Purpose: Class representing the standard room.
    
    """
    def __init__(self):
        """Intializes the room object with given room_type.

        Args:
            room_type: The type of the room.
            room_price: price of each room excluding any additional amenities.
        """
        super().__init__("Super Deluxe", 509)