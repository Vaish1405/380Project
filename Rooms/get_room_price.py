from .Standard import StandardRoom
from .Deluxe import DeluxeRoom
from .SuperDeluxe import SuperDeluxeRoom

def get_room_price(selection):
    """Function that is delegated the task of getting the room prices. 

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
    
