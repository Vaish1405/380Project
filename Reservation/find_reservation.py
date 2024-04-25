import pandas as pd

def find_reservation(user_name, check_in, check_out):
    """
    Programmer: Vaishnavi Sen
    
    Purpose: Function to get the reservation details for a given person.  

    Args:
        user_name: User's name for which the reservation is being retrieved. 
        check_in: Start date of the reservation. 
        check_out: End date of the reservation. 

    Returns:
        reservation_data: array containing all the reservation details. 
    """
    read_data = pd.read_csv('data/reservations.csv')
    reservation_data = read_data[(read_data['user_name'] == user_name) & 
                                 (read_data['check_in'] == check_in) & 
                                 (read_data['check_out'] == check_out)]

    return reservation_data