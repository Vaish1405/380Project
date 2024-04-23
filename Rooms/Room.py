class Room():
    """Class for different types of rooms.""" 
    def __init__(self, room_type, room_price):
        """Intializes the room object with given roomType

        Args:
            room_type: The type of the room.
            room_price: price of each room excluding any additional amenities.
        """
        self.room_type = room_type
        self.room_price = room_price
    
    def get_price(self):
        """Method to retrieve the price of the requested room. 

        Returns:
            int: Room price for each type.
        """
        return self.room_price