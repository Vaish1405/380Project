class shuttle():
    """Class representing the shuttle services provided for extra amenities."""
    def get_price(self):
        """Get price of adding shuttle service to the reservation.

        Returns:
            int: total price of the shuttle service.
        """
        return 100
    
class ExtraService(): 
    """Class for creating new extra amenities offered to the users during the reservation option."""
    def __init__(self, service_type, service_cost): 
        """Intializes the room object with given roomType

        Args:
            service_typ: The type of the services provided. 
            service_cost: Price of the provided service.
        """
        self.service_type = service_type
        self.service_cost = service_cost

    def get_price(self):
        """Method to retrieve the price of the requested room. 

        Returns:
            int: Room price for each type.
        """
        return self.service_cost