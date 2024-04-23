class ExtraService(): 
    """
    Programmer: Vaishnavi Sen
    
    Purpose: Class for creating new extra amenities offered to the users during the reservation option.
    
    """
    def __init__(self, service_type, service_cost): 
        """Intializes the room object with given roomType

        Args:
            service_typ: The type of the services provided. 
            service_cost: Price of the provided service.
        """
        self.service_type = service_type
        self.service_cost = service_cost

    def get_price(self):
        """Method to retrieve the price of the requested service. 

        Returns:
            int: Price for adding each requested service.
        """
        return self.service_cost