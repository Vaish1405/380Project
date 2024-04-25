from .Room import Room

class DeluxeRoom(Room):
    """Class representing the standard room."""
    def __init__(self):
        """
        Programmer: Vaishnavi Sen

        Purpose: Intializes the room object with given room_type.

        Args:
            room_type: The type of the room.
            room_price: price of each room excluding any additional amenities.
        """
        super().__init__("Deluxe", 309)