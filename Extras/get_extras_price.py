from .Pet import Pet
from .Shuttle import Shuttle

def get_extras_price(selection):
    """Function that is delegated the task of getting the price for selected amenities. 

    Args:
        selection: The type of amenities selected (Pet or Shuttle).

    Returns:
        int: The price of the selected service, or 0 if the selected option is invalid.
    """
    selection = selection.lower()
    if selection == "pet":
        return Pet().get_price()
    elif selection == "shuttle":
        return Shuttle().get_price()
    else:
        return 0