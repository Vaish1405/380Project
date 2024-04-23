import pandas as pd

def find_reservation(user_name, check_in, check_out):
    """
    Programmer: Vaishnavi Sen
    
    Purpose: Function that is delegated the task of getting the price for selected amenities. 

    Args:
        selection: The type of amenities selected (Pet or Shuttle).

    Returns:
        int: The price of the selected service, or 0 if the selected option is invalid.
    """
    read_data = pd.read_csv('data/reservations.csv')
    reservation_data = read_data[(read_data['user_name'] == user_name) & 
                                 (read_data['check_in'] == check_in) & 
                                 (read_data['check_out'] == check_out)]

    return reservation_data