from .ExtraService import ExtraService

class Shuttle(ExtraService):
    """
    Programmer: Vaishnavi Sen
    
    Purpose: Class representing the details of shuttle reservation.
    
    """
    def __init__(self):
        """Intializes the Shuttle object to indicate the price."""
        super().__init__("Shuttle", 100)