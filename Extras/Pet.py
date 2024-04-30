from .ExtraService import ExtraService

class Pet(ExtraService):
    """
    Programmer: Vaishnavi Sen
    
    Purpose: Class representing the details of Pet reservation.
    
    """
    def __init__(self):
        """Intializes the Pet object to indicate the price."""
        super().__init__("Pet", 200)