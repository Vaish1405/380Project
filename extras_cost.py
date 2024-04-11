class shuttle():
    """Class representing the shuttle services provided for extra amenities."""
    def get_price(self):
        """Get price of adding shuttle service to the reservation.

        Returns:
            int: total price of the shuttle service.
        """
        return 100
    
class pet():
    """Class representing the pet service provided for extra amenities."""
    def get_price(self):
        """Get price of adding pet services to the reservation.

        Returns:
            int: total price for adding a pet to the reservation.
        """
        return 200
    
def get_extras_price(selection):
    """Controller function to get the price selected extra amenities by the user.

    Args:
        selection: The type of service chosen (Shuttle or Pet).

    Returns:
        int: The price of the selected service. 0 if the selection is invalid or no choice is selected.
    """
    selection = selection.lower()
    if selection == "shuttle":
        return shuttle().get_price()
    elif selection == "pet":
        return pet().get_price()
    else: 
        return 0